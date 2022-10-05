d1 = int(input("Введите день рождения "))
m1 = int(input("Введите месяц рождения "))
y1 = int(input("Введите год рождения "))
d2 = int(input("Введите сегодняшний день "))
m2 = int(input("Введите сегодняшний месяц "))
y2 = int(input("Введите сегодняшний год "))
y = y2-y1
if m2 < m1 and d1 == d2:
    year = y-1
    print("Полных лет", year)
elif m2 == m1 and d2 < d1:
    year = y - 1
    print("Полных лет", year)
elif m2 < m1 and d2 < d1:
    year = y - 1
    print("Полных лет", year)
elif m2 == m1 and d2 == d1:
    print("Полных лет", y)
else:
    print("Полных лет", y)
