try:
    ch1 = int(input("Введите пятизначное натуральное число "))
    if 9999 < ch1 < 100000:
        if int(str(ch1)[0]) > 8 or int(str(ch1)[1]) > 8 or int(str(ch1)[2]) > 8 or int(str(ch1)[3]) > 8 or int(str(ch1)[4]) > 8:
            print("Наибольшая цифра в данном числе 9")
        elif 9>int(str(ch1)[0])>7 or 9>int(str(ch1)[1])>7 or 9>int(str(ch1)[2])>7 or 9>int(str(ch1)[3])>7 or 9>int(str(ch1)[4])>7:
            print("Наибольшая цифра в данном числе 8")
        elif 8>int(str(ch1)[0]) > 6 or 8>int(str(ch1)[1]) > 6 or 8>int(str(ch1)[2]) > 6 or 8>int(str(ch1)[3]) > 6 or 8>int(str(ch1)[4]) > 6:
            print("Наибольшая цифра в данном числе 7")
        elif 7>int(str(ch1)[0]) > 5 or 7>int(str(ch1)[1]) > 5 or 7>int(str(ch1)[2]) > 5 or 7>int(str(ch1)[3]) > 5 or 7>int(str(ch1)[4]) > 5:
            print("Наибольшая цифра в данном числе 6")
        elif 6>int(str(ch1)[0]) > 4 or 6>int(str(ch1)[1]) > 4 or 6>int(str(ch1)[2]) > 4 or 6>int(str(ch1)[3]) > 4 or 6>int(str(ch1)[4]) > 4:
            print("Наибольшая цифра в данном числе 5")
        elif 5>int(str(ch1)[0]) > 3 or 5>int(str(ch1)[1]) > 3 or 5>int(str(ch1)[2]) > 3 or 5>int(str(ch1)[3]) > 3 or 5>int(str(ch1)[4]) > 3:
           print("Наибольшая цифра в данном числе 4")
        elif 4>int(str(ch1)[0]) > 2 or 4>int(str(ch1)[1]) > 2 or 4>int(str(ch1)[2]) > 2 or 4>int(str(ch1)[3]) > 2 or 4>int(str(ch1)[4]) > 2:
            print("Наибольшая цифра в данном числе 3")
        elif 3>int(str(ch1)[0]) > 1 or 3>int(str(ch1)[1]) > 1 or 3>int(str(ch1)[2]) > 1 or 3>int(str(ch1)[3]) > 1 or 3>int(str(ch1)[4]) > 1:
            print("Наибольшая цифра в данном числе 2")
        elif 2>int(str(ch1)[0]) > 0 or 2>int(str(ch1)[1]) > 0 or 2>int(str(ch1)[2]) > 0 or 2>int(str(ch1)[3]) > 0 or 2>int(str(ch1)[4]) > 0:
            print("Наибольшая цифра в данном числе 1")
    else: print("Введено неверное число")
except: print("Введено неверное число")
