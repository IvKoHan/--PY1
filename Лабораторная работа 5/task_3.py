from random import randint, sample


def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) != 15:
        num = randint(-10, 10)
        if num not in list_:
            list_.append(num)

    return list_


# Эта функция аналогична get_unique_list_numbers(), но с применением функции random.sample()
def get_unique_list_numbers2() -> list[int]:
    return [num for num in sample(range(-10, 10), 15)]


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

list_unique_numbers2 = get_unique_list_numbers2()
print(list_unique_numbers2)
print(len(list_unique_numbers2) == len(set(list_unique_numbers2)))
