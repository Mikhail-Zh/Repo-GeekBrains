list_ending = ["а", "ов"]  # Создание списка окончаний
percent = "процент"
for i in range(1, 101):  # Цикл для вывода
    if i % 10 == 1 and i % 100 != 11:  # Исключение 11. % 100 для исключения при диапозоне больше чем 100 процентов.
        print(i, percent)
    elif 2 <= i % 10 <= 4 and i % 100 != 12 and i % 100 != 13 and i % 100 != 14:  # Исключение 12, 13, 14
        print(i, percent + list_ending[0])
    else:  #
        print(i, percent + list_ending[1])
