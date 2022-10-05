try:
    a = int(input("Введите число a "))
    b = int(input("Введите число b "))
    c = a-b
    d = a/b
except(ValueError, ZeroDivisionError):
    print("Возможно где-то ошибка...")
else:
    print(c)
    print(d)
