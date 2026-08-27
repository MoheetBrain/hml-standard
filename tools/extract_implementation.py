"""Extract the frozen semantic inventory from the executable implementation.

The Standard describes frozen executable semantics; it does not invent them. So the
dictionary, the machine artifacts and the traceability matrix are all *derived* from this
extraction rather than transcribed by hand. If the implementation changes, the extraction
changes, and the audits fail until the Standard is updated to match.

    python tools/extract_implementation.py <path-to-hamiltonian-lang> > machine/_extracted.json
"""

from __future__ import annotations

import dataclasses
import enum
import inspect
import json
import subprocess
import sys
from pathlib import Path


def _src(obj) -> dict:
    try:
        file = inspect.getsourcefile(obj)
        line = inspect.getsourcelines(obj)[1]
        return {"file": file, "line": line}
    except Exception:
        return {"file": None, "line": None}


def _rel(path: str | None, root: Path) -> str | None:
    if not path:
        return None
    try:
        return str(Path(path).resolve().relative_to(root.resolve()))
    except Exception:
        return path


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    sys.path.insert(0, str(root / "src"))

    from hamiltonian_lang.reasoning import kernel
    from hamiltonian_lang.semantic_state import model as M
    from hamiltonian_lang import types as T

    # Record the commit, not the local path. The path is a property of whoever ran the
    # extraction; the commit is a property of what was extracted, and this file is
    # published.
    try:
        commit = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                                capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        commit = "unknown"
    out: dict = {"source_commit": commit}

    # ---- kernel inference rules -------------------------------------------
    rules = []
    for name in kernel.rule_names():
        spec = kernel.RULES[name]
        entry = {"name": name}
        for f in dataclasses.fields(spec):
            v = getattr(spec, f.name)
            if callable(v):
                v = getattr(v, "__name__", "<callable>")
            elif isinstance(v, tuple):
                v = [str(x) if not isinstance(x, (str, int, float, bool, type(None))) else x
                     for x in v]
            elif not isinstance(v, (str, int, float, bool, type(None), list, dict)):
                v = str(v)
            entry[f.name] = v
        rules.append(entry)
    out["kernel_rules"] = rules
    out["kernel_rule_count"] = len(rules)

    # ---- semantic state records -------------------------------------------
    records = []
    for name in dir(M):
        obj = getattr(M, name)
        if not dataclasses.is_dataclass(obj) or not isinstance(obj, type):
            continue
        fields = []
        for f in dataclasses.fields(obj):
            default = None
            has_default = False
            if f.default is not dataclasses.MISSING:
                default = f.default
                has_default = True
            elif f.default_factory is not dataclasses.MISSING:  # type: ignore[misc]
                default = f.default_factory()                    # type: ignore[misc]
                has_default = True
            if isinstance(default, enum.Enum):
                default = default.value
            if isinstance(default, tuple):
                default = list(default)
            fields.append({
                "name": f.name,
                "type": f.type if isinstance(f.type, str) else str(f.type),
                "has_default": has_default,
                "default": default if isinstance(
                    default, (str, int, float, bool, type(None), list, dict)) else str(default),
            })
        loc = _src(obj)
        records.append({
            "name": name,
            "frozen": obj.__dataclass_params__.frozen,
            "fields": fields,
            "doc": (inspect.getdoc(obj) or "").split("\n\n")[0],
            "file": _rel(loc["file"], root),
            "line": loc["line"],
        })
    out["state_records"] = sorted(records, key=lambda r: r["name"])

    # ---- enumerations (the status vocabularies) ---------------------------
    enums = []
    for name in dir(M):
        obj = getattr(M, name)
        if isinstance(obj, type) and issubclass(obj, enum.Enum) and obj is not enum.Enum:
            loc = _src(obj)
            enums.append({
                "name": name,
                "members": [m.value for m in obj],
                "doc": (inspect.getdoc(obj) or "").split("\n\n")[0],
                "file": _rel(loc["file"], root),
                "line": loc["line"],
            })
    out["enumerations"] = sorted(enums, key=lambda e: e["name"])

    # ---- type system ------------------------------------------------------
    tnames = []
    for name in dir(T):
        obj = getattr(T, name)
        if isinstance(obj, type) and obj.__module__.startswith("hamiltonian_lang"):
            loc = _src(obj)
            tnames.append({
                "name": name,
                "is_enum": issubclass(obj, enum.Enum),
                "members": ([m.value for m in obj] if issubclass(obj, enum.Enum)
                            and obj is not enum.Enum else None),
                "doc": (inspect.getdoc(obj) or "").split("\n")[0],
                "file": _rel(loc["file"], root),
                "line": loc["line"],
            })
    out["types"] = sorted(tnames, key=lambda t: t["name"])

    # ---- backends ---------------------------------------------------------
    backends = []
    bdir = root / "src" / "hamiltonian_lang" / "backends"
    for p in sorted(bdir.glob("*.py")):
        if p.stem.startswith("_"):
            continue
        backends.append({"name": p.stem, "file": _rel(str(p), root)})
    out["backends"] = backends

    # ---- libraries --------------------------------------------------------
    libs = []
    ldir = root / "src" / "hamiltonian_lang" / "libraries"
    for p in sorted(ldir.glob("*.py")):
        if p.stem.startswith("_"):
            continue
        libs.append({"name": p.stem, "file": _rel(str(p), root)})
    out["libraries"] = libs

    json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
