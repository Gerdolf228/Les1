try:
    print("Пример ввода даты рождения 08.11.1999")
    data1 = input("Введите дату рождения первого человека ")
    data2 = input("Введите дату рождения второго человека ")
    if int(data1[6:10:1]) < int(data2[6:10:1]):
        print("Первый человек старше")
    elif int(data1[6:10:1]) > int(data2[6:10:1]):
        print("Второй человек старше")
    elif int(data1[6:10:1]) == int(data2[6:10:1]) and int(data1[3:5:1]) < int(data2[3:5:1]):
        print("Первый человек старше")
    elif int(data1[6:10:1]) == int(data2[6:10:1]) and int(data1[3:5:1]) > int(data2[3:5:1]):
        print("Второй человек старше")
    elif int(data1[6:10:1]) == int(data2[6:10:1]) and int(data1[3:5:1]) == int(data2[3:5:1]) and int(data1[0:2:1]) < int(data2[0:2:1]):
        print("Первый человек старше")
    elif int(data1[6:10:1]) == int(data2[6:10:1]) and int(data1[3:5:1]) == int(data2[3:5:1]) and int(data1[0:2:1]) > int(data2[0:2:1]):
        print("Второй человек старше")
except:
    print("Ошибка ввода")
