def get_count_char(str_):  # функция для нахождения количества букв
    dict_of_letters = {}
    count = 0

    for letter in str_.lower():
        if letter.isalpha():
            dict_of_letters[letter] = dict_of_letters.get(letter, count) + 1

    return dict_of_letters


def get_interest(dict_):  # функция для нахождения процента
    dict_interest = {}
    value = sum(dict_.values())

    for letter, count in dict_.items():
        dict_interest[letter] = round(count / value * 100, 2)

    return dict_interest


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

f = get_count_char(main_str)

print(f)
print(get_interest(f))
