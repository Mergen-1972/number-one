sh = int(input("Введите нужное количество билетов:" ))


s=0
if 0<sh < 3:

    a = int(input("Введите количество участников старше 18 лет:"))
    b = int(input("Введите количество участников старше 25:"))

    xyz=a*990 + b*1390
    summ= xyz
    print (summ)

elif sh>3:

    a = int(input("Введите количество участников старше 18 лет:"))
    b = int(input("Введите количество участников старше 25:"))

    xyz = a * 990 + b * 1390
    summ=xyz*0.9
    print(summ)

else:

    print("введите правильное количество билетов")