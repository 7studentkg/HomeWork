print('Home Work №2\nЗнаки Задиака')


day = int(input('Введите день рождения: '))
month = int(input('Введите месяц рождения: '))


if day == 0 :
   print("ERROR BRO\nПример >>\nДень рождения: '19'\nМесяц: '8'\nВыводить >>\nЗнак зодиака: 'Лев'")


elif ( 21 <= day <= 31 and month == 3) or (day <=20 and month == 4 ):
   print("Знак зодиака: Овен")

elif ( 21 <= day <= 30 and month == 4 ) or (day <=21 and month == 5 ):
   print("Знак зодиака: Телец")

elif ( 22 <= day <= 31 and month == 5) or (day <=21 and month == 6 ):
   print("Знак зодиака: Близнецы")

elif ( 22 <= day <= 30 and month == 6) or (day <= 22 and month == 7 ):
   print("Знак зодиака: Рак")

elif ( 23 <= day <= 31 and month == 7) or (day <= 21 and month == 8 ):
   print("Знак зодиака: Лев")

elif ( 22 <= day <= 31 and month == 8) or (day <= 23 and month == 9 ):
   print("Знак зодиака: Дева")

elif ( 24 <= day <= 30 and month == 9) or (day <= 23 and month == 10 ):
   print("Знак зодиака: Весы")

elif ( 24 <= day <= 31 and month == 10) or (day <= 22 and month == 11 ):
   print("Знак зодиака: Скорпион")

elif (day >= 23 and day <= 30 and month == 11) or (day <= 22 and month == 12 ):
   print("Знак зодиака: Стрелец")

elif (day >= 23 and day <= 31 and month == 12) or (day <= 20 and month == 1 ):
   print("Знак зодиака: Козерог")

elif (day >= 21 and day <= 31 and month == 1) or (day <= 19 and month == 2 ):
   print("Знак зодиака: Водолей")

elif (day >= 20 and day <= 28 and month == 2) or (day <= 20 and month == 3 ):
   print("Знак зодиака: Рыбы")


else:
   print("ERROR BRO\nПример >>\nДень рождения: '19'\nМесяц: '8'\nВыводить >>\nЗнак зодиака: 'Лев'")
