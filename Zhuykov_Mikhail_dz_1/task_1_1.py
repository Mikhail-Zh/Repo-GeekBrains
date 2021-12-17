duration = int(input("Введите период времени: "))                          # Определение duration для варианта №1

print("Вариант №1. Ветвление")

if duration // 86400:                                                      # Вычисление количества дней
    print(duration // 86400, "дн ", end='')
    duration %= 86400
if duration // 3600:                                                       # Вычисление количества часов
    print(duration // 3600, "час ", end='')
    duration %= 3600
if duration // 60:                                                         # Вычисление количества минут
    print(duration // 60, "мин ", end='' )
    duration %= 60
if duration % 60:                                                          # Вычисление количества секунд
    print(duration % 60, "сек")
print()

# _______________________________________________________________
# _______________________________________________________________

duration = int(input("Введите период времени: "))                          # Определение duration для варианта №2

print("Вариант №2. Цикл. Применение словаря")

day = duration // 86400                                                    # Вычисление количества дней
hour = duration % 86400 // 3600                                            # Вычисление количества часов
minute = duration % 86400 % 3600 // 60                                     # Вычисление количества минут
second = duration % 60                                                     # Вычисление количества секунд
time = {"дн ": day, "час ": hour, "мин ": minute, "сек": second}           # Создание словаря
for k, v in time.items():                                                  # цикл для выдачи не нулевых периодов
    if v != 0:
        print(v, k, end='')
print()

# _______________________________________________________________
# _______________________________________________________________

print("\nВариант №3. Цикл. Применение списка. duration из списка")

duration = [1233, 459099, 63748, 29, 278]                                     # Создание списка duration

for k in range(len(duration)):                                                # цикл для перебора нескольких периодов
    day = duration[k] // 86400                                                # Вычисление количества дней
    hour = duration[k] % 86400 // 3600                                        # Вычисление количества часов
    minute = duration[k] % 86400 % 3600 // 60                                 # Вычисление количества минут
    second = duration[k] % 60                                                 # Вычисление количества секунд
    period = ["дн ", "час ", "мин ", "сек"]                                   # Создание списка с именами периодов
    time = [day, hour, minute, second]                                        # Создание списка с периодами
    for i in range(len(time)):                                                # цикл для выдачи не нулевых периодов
        if time[i] != 0:
            print(time[i], period[i], end='')
    print()                                                                   # для перевода строки

# _______________________________________________________________
# _______________________________________________________________

