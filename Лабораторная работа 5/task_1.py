from pprint import pprint


def list_of_number_systems(start: int = 0, stop: int = 15) -> list:
    if not isinstance(start, int):
        raise TypeError(f"Первое число должно быть типом int, а не {type(start)}.")
    if not isinstance(stop, int):
        raise TypeError(f"Второе число должно быть типом int, а не {type(stop)}.")

    list_ = []

    for num in range(start, stop + 1):
        dict_ = {
            'bin': bin(num),
            'oct': oct(num),
            'dec': num,
            'hex': hex(num)
        }
        list_.append(dict_)

    return list_


pprint(list_of_number_systems())
pprint(list_of_number_systems(4, 19))
