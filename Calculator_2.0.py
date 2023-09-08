print ("Hello buddy\nHow are you ?" )

# print("Percent ")
#
# x = float(input ('x='))
#
# y = float (input ('y='))
# print('Answer = '+ str(  x*y / 100) )
#choice = input('p if percentage c if calculator or b ')
#
#prodolzhit  = 'k'
# while prodolzhit == 'k' :
#
    # ab = float ( input ("Ведите первое число >>"))
    # oper = input("Ввод операций >>")
    # cd = float ( input ("Ведите второе число >>"))
    # if oper == '+' :
            # print(ab + cd)
    # elif oper == '-':
            # print(ab - cd)
    # elif oper == '*':
            # print(ab*cd)
    # elif oper == '/':
            # print(ab/cd)
    # elif oper :
            # print('Error')
    # prodolzhit = input("Продолжить 'k' or завершить любая клавиша ")

choice = input('p if percentage c if calculator or b ')

prodolzhit  = 'k'

while True:
    if choice == 'p':
        x = float(input ('x='))
        y = float (input ('y='))
        print('Answer = '+ str(  x*y / 100) )
        choice = input('p if percentage c if calculator or b')




    elif choice == 'b':
            print('pashol nahui :)')
            break # останавливает цикл


    elif choice == 'c':
        ab = float ( input ("Ведите первое число >>"))
        oper = input("Ввод операций >>")
        cd = float ( input ("Ведите второе число >>"))
        if oper == '+' :
                print(ab + cd)
        elif oper == '-':
                print(ab - cd)
        elif oper == '*':
                print(ab*cd)
        elif oper == '/':
                print(ab/cd)
        elif oper == '**':
                print(ab**cd)
        elif oper :
                print('Error')
        choice = input('p if percentage c if calculator or b')
