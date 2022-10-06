a = int(input("Введите пятизначное число: "))
if 9999 < a < 100000:
    m = 0
    a = str(a)
    for i in a:
        if int(i) > m:
            m = int(i)
    print(m)
else: print("Введено неверное число")