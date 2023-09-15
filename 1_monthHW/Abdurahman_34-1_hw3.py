print("Home Work №3\n")

a = 0 # чётное число
b = 0 # нечётное число

while a < 50 > b:

    enter = int(input("Введите число: "))
    if enter == 42 :
        break

    elif enter % 5 == 0:
        print("кратное 5")
        if enter % 2 == 0:
            print("чётное число")
            a += enter
        else:
            print("не чётное число")
            b += enter

    elif enter % 2 == 0:
        print("чётное число")
        a += enter

    else:
        print("не чётное число")
        b += enter

    print(f"Ячейка 'a' чётное >> {a}")
    print(f"Ячейка 'b' нечётное >> {b}")


    #
# print("Home Work №3.2\n")
#
# a = 0 # чётное число
# b = 0 # нечётное число
#
# while a < 50 > b:
#
    # enter = int(input("Введите число: "))
    # if enter == 42 :
        # break
#
    # elif enter % 5 == 0:
        # print("кратное 5")
#
    # if enter % 2 == 0:
        # print("чётное число")
        # a += enter
#
    # if enter % 2 > 0 :
        # print("не чётное число")
        # b += enter
#
    # print(f"Ячейка 'a' чётное >> {a}")
    # print(f"Ячейка 'b' нечётное >> {b}")
#
#
