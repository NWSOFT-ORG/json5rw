from typing import Callable, TextIO

from src.decoder import Decoder
from src.parser import (
    parse,
)
from src.default_processing import (
    process_constant, process_float, process_int, process_object_hook,
    process_object_pairs_hook,
)
from src.convert_standard import convert_standard


def load(
    fp: TextIO,
    *,
    object_hook: Callable = process_object_hook,
    parse_float: Callable = process_float,
    parse_int: Callable = process_int,
    parse_constant: Callable = process_constant,
    object_pairs_hook: Callable = process_object_pairs_hook
):
    with fp:
        content = fp.read()
        content = convert_standard(content)
        return parse(content, Decoder(), object_hook, parse_float, parse_int, parse_constant, object_pairs_hook)


def loads(
    s: str,
    *,
    object_hook: Callable = process_object_hook,
    parse_float: Callable = process_float,
    parse_int: Callable = process_int,
    parse_constant: Callable = process_constant,
    object_pairs_hook: Callable = process_object_pairs_hook
):
    s = convert_standard(s)
    return parse(s, Decoder(), object_hook, parse_float, parse_int, parse_constant, object_pairs_hook)
