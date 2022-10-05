try:
    ch1 = int(input("Введите минимум "))
    ch2 = int(input("Введите максимум "))
    ch3 = int(input("Введите шаг "))
    for fif in range(ch1, ch2+1, ch3):
        print(fif, end=" ")
except:
    print("Введено не целое число")