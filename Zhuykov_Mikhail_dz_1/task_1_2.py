def numbers_divided_by_7(lst):
    """
    Фунция определяет делится ли на 7 сумма цифр в каждом числе списка
    :param lst: Список чисел
    :return: Возвращает список чисел сумма цифр которых делится на 7.
    """
    result = []  # Объявление переменной
    for i in range(len(lst)):  # Цикл перебора списка lst_cubes
        sum_el = 0
        division = lst[i]
        while True:  # Цикл перебора элементов списка lst_cubes
            sum_el += division % 10
            division = division // 10
            if division == 0:
                break
        if sum_el % 7 == 0:  # Определение деления элемента списка на 7
            result.append(lst[i])
    return result


def adding_a_number(lst, number=17):
    """
    Функция для прибавления числа к каждому элементу в списке.
    :param lst: Список чисел
    :param number: По умолчанию 17. Число которое требуется прибавить к элементам списка.
    :return: Возращает список
    """
    lst = [i + number for i in lst]
    return lst


print("Список кубов нечетных чисел от 1 до 1000")
lst_cubes = [i ** 3 for i in range(1, 1000, 2)]  # Создание списка кубов нечетных чисел от 1 до 1000
print(lst_cubes)

print("Задание под буквой а")  # Задание под буквой а

print(numbers_divided_by_7(lst_cubes))

print("Задание под буквой b")  # Задание под буквой b

print(numbers_divided_by_7(adding_a_number(lst_cubes, 17)))
