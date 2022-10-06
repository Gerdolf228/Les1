try:
    ch1 = int(input("Введите число "))
    ch2 = int(str(ch1)[::-1])
    print(ch2)
except:
    print("Введено неверно!")