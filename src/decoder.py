from src.default_processing import (
    process_float, process_int, process_constant, process_object_hook,
    process_object_pairs_hook,
)


class Decoder:
    parse_float = staticmethod(process_float)
    parse_int = staticmethod(process_int)
    parse_constant = staticmethod(process_constant)
    object_hook = staticmethod(process_object_hook)
    object_pairs_hook = staticmethod(process_object_pairs_hook)
