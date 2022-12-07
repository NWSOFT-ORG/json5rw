import json
from typing import TextIO

from src.loader import loads


def dump(
    obj: dict,
    fp: TextIO,
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: json.JSONEncoder = None,
    indent=None,
    separators=None,
    default=None,
    sort_keys: bool = False
):
    json.dump(
        obj, fp, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan,
        cls=cls, indent=indent, separators=separators, default=default, sort_keys=sort_keys
    )


def dumps(
    s: str,
    fp: TextIO,
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: json.JSONEncoder = None,
    indent=None,
    separators=None,
    default=None,
    sort_keys: bool = False
):
    obj = loads(s)
    with fp:
        dump(
            obj, fp, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan,
            cls=cls, indent=indent, separators=separators, default=default, sort_keys=sort_keys
        )
