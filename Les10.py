try:
    ch1 = int(input("Введите трехзначное число: "))
    if 99 < ch1 < 1000:
        sum = int(str(ch1)[0]) + int(str(ch1)[1]) + int(str(ch1)[2])
        print(sum)
        proiz = int(str(ch1)[0]) * int(str(ch1)[1]) * int(str(ch1)[2])
        print(proiz)
    else:
        print("Число не трехзначное")
except ValueError:
    print("Введено не трехзначное число")