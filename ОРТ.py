print("ОРТ - Общереспубликанского тестирования")
#
#math = float ( input ("Математика "))
#
#reading_language = float ( input ("Аналогия и Грамматика "))
#
#result1 = math * 1.1
#
#result2 = reading_language * 2
#
#result3 = round (result1 + result2)
#
#print ("Результат :  "  + str(result3)  + " балл из 245 " )

#
#print("ОРТ - Общереспубликанского тестирования")
#
#while True :
#
#    math = float ( input ("Математика: "))
#
#    reading_language = float (input("Аналогия и Грамматика: "))
#
#    result1 = math * 1.1
#
#    result2 = reading_language * 2
#
#    result3 = round (result1 + result2)
#
#    if  result3 > 245 :
#        print("Error because result > 245")
#        break
#
#    if result3 >= 220 :
#        print("Gold certificate")
#
#    if math == 1:
#        print("Good luck")
#        break
#
#    print ("Результат :  "  + str(result3)  + " балл из 245 " )

print(60000/5)

while True :

    math = float ( input ("Математика: "))

    reading = float(input("Аналогия и Чтение: "))

    language = float (input("Грамматика: "))

    result1 = math * 1.1

    result2 = reading * 2.016

    result3 = language * 1.9

    result4 = round (result1 + (result2 + result3))
    if  result4 > 245 :
        print("Error, because result > 245")
        break

    if result4 >= 220 :
        print("Gold certificate")

    if math == 1:
        print("Good luck")
        break

   # if math > 60 :
   #     print("Error")
   #     break
#
   # if reading > 60 :
   #     print("Error")
   #     break
#
   # if language > 30 :
   #     print("Error")
   #     break

    print ("Результат :  "  + str(result4)  + " балл из 245 " )
