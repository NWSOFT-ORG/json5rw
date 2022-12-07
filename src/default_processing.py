def process_float(item: float):
    return float(item)


def process_int(item: int):
    return int(item)


def process_constant(item: float):
    return float(item)


def process_object_hook(item: dict):
    return item


def process_object_pairs_hook(item: dict):
    values = []
    for key, value in item.items():
        values.append((key, value))
