import json
import warnings
from typing import Any

from src.default_processing import (
    process_constant, process_float, process_int, process_object_hook, process_object_pairs_hook,
)


class Encoder(json.JSONEncoder):
    item_separator = ', '
    key_separator = ': '

    def __init__(
        self, *, skipkeys=False, ensure_ascii=True,
        check_circular=True, allow_nan=True, sort_keys=False,
        indent=None, separators=None, default=None
    ):
        super().__init__(
            skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan,
            sort_keys=sort_keys, indent=indent, separators=separators, default=default
        )

    def default(self, o: Any) -> Any:
        warnings.warn(f"Object of type {o.__class__.__name__} cannot be serialized into JSON")

    parse_float = staticmethod(process_float)
    parse_int = staticmethod(process_int)
    parse_constant = staticmethod(process_constant)
    object_hook = staticmethod(process_object_hook)
    object_pairs_hook = staticmethod(process_object_pairs_hook)
