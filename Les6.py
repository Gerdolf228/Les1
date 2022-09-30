n = int(input("Введите возраст "))
konec = n % 10    # Остаток деления на 10
if 1 <= n <= 99:
    if 10 < n < 20:
        print("Мне", n, "лет")
    elif 4 < konec < 10:
        print("Мне", n, "лет")
    elif konec == 0:
        print("Мне", n, "лет")
    elif 1 < konec < 5:
        print("Мне", n, "года")
    elif konec == 1:
        print("Мне", n, "год")
else:
    print("Возраст за рамками диапазона от 1 до 99")
