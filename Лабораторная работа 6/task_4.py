import json

INPUT_FILE = "input.csv"


# TODO реализовать конвертер из csv в json
def csv_to_list_dict(filename: str, delimiter: str = ",", new_line: str = "\n") -> list[dict]:
    if not isinstance(filename, str):
        raise TypeError(f"Название файла должно быть типом str, а не {type(filename)}.")

    if not isinstance(delimiter, str):
        raise TypeError(f"Разделитель между значениями для файла csv должен быть типом str, а не {type(delimiter)}.")

    if not isinstance(new_line, str):
        raise TypeError(f"Разделитель между строками для файла csv должен быть типом str, а не {type(new_line)}.")

    with open(filename) as f:

        read = [line.split(delimiter) for line in f.read().split(new_line) if line]
        dict_ = {meaning: i for i, meaning in enumerate(read[0])}
        list_ = []

        for part in read[1:]:
            dict_copy = dict_.copy()

            for key, value in dict_copy.items():
                dict_copy[key] = part[value]

            list_.append(dict_copy)

        return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
