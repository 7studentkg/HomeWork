""" ​‌‍‌‍Lesson 1 " Hello, World " / Text​​"""
print("I will show you Magic")
print("Are you ready?") # ⁡⁢⁢⁡⁣⁢⁢Ok I'm joking⁡⁡
#⁡⁣⁢ ⁡⁣⁢⁢I will show you how work python, but it's not python what you think now ,⁡
#⁡⁣⁡⁣⁢⁢ This basic code , here we will work with math , yes us need math , don't cry buddy ,⁡⁡
# ⁡⁣⁢⁢Not only math , we will use our logic⁡
# ⁡⁣⁢⁢We will think , this spend most time Than math , yeah I'm not joking⁡

print()

#print('"Kevin\'s favorite word is "Women""') # ⁡⁢⁣⁢если мы хотим в тескте кавычки то делаем это так⁡
#
#print()
#
## ⁡⁢⁣⁢Если мы хотим последовательность то мы use { \n }⁡
#print ('I see you\nYou see me\nHow pleasent\nThis feeling ')
## ⁡⁢⁢⁢у нас должно выйти это⁡
## ⁡⁣⁣⁢𝗜 𝘀𝗲𝗲 𝘆𝗼𝘂⁡
## ⁡⁣⁣⁢𝗬𝗼𝘂 𝘀𝗲𝗲 𝗺𝗲⁡
## ⁡⁣⁣⁢𝗛𝗼𝘄 𝗽𝗹𝗲𝗮𝘀𝗲𝗻𝘁⁡
## ⁡⁣⁣⁢𝗧𝗵𝗶𝘀 𝗳𝗲𝗲𝗹𝗶𝗻𝗴⁡
#
#print()
#print ("Begin") # Text
#print ("\n") # ⁡⁢⁣⁢Строка с невидимым символом перевода строки ,мы увидем две пустые строки⁡
#print ("End") # Text
#
#print()
#
## ⁡⁢⁣⁢объединение текста⁡
#print('Butter'+'fly') # Сливочное масло + летать = Бабочка #Butterfly
#
#print()
#
## ⁡⁢⁣⁢если хотим что бы меджу словами был пробел ...⁡
#print ('I Know' + ' you want' + ' me baby' )
#
#print()
#
#​‌‍‌⁡⁢⁣⁢ Lesson 2 / Переменные ⁡​
## ⁡⁣⁢⁣Переменная — это простейшая именованная структура данных ,⁡
## ⁡⁣⁢⁣в которой может быть сохранён промежуточный или конечный результат работы программы.⁡
#
#
#lesson2 = "Переменная "
#lesson_2 ="— это простейшая именованная структура данных"
#print ( lesson2 + lesson_2 )
#
#
## ⁡⁢⁣⁢Мы можем писать имена/переменные в пару стилях⁡
#
#name = 1
#Name = 2
#NaMe = 3
#MyName = NaMe
#my_name = 4
#My_name = my_name
#My_Name = My_name
#day = "5/365"
#day2 = day
#day3 = day2
#
#print (name)
#print (Name)
#print (MyName)
#print (My_Name)
#print (day3)
#
#print()
#
## ⁡⁢⁣⁣Если мы хотим + переменную с текстом , use { f' {} '}⁡
## ⁡⁣⁢⁣Буква f указывает на то, что мы создаем f-строку — шаблон,⁡
## ⁡⁣⁢⁣в который с помощью фигурных скобок подставляются значения переменных.⁡
#
#Day = 365
#Year = f'{Day} days in a year'
#
#print (Year)
#
## ⁡⁢⁣⁣если мы попытаемся + перемуную и текст или число будет Error⁡
## x = 123
## y = "four five six"
## z = x + y
## print( z )
#
#print()
#
## ⁡⁢⁣⁢Преставьте что у вас есть текст или числа из них вам нужно вывести на экран первую букву или число⁡
#
#number_0 = "David"
## ⁡⁢⁣⁢первая буква в ⁡⁣⁢⁢⁡⁢⁣⁢index будет знчаить [0] etc⁡⁡
#print (number_0 [0]) # => D
## ⁡⁢⁣⁢если хотим видеть последнию букву вместо того что считать какой index буквы мы можем сделать так⁡
#print(number_0[-1]) # => d
## ⁡⁢⁣⁣До вас дашло как это работает , Думайте хорошенко⁡
#
#print()
#
#date = '18-12-2022'
#
#print(date[6])  # => 2
#print(date[9])  # => 4
#
#print()
#
#year = date[6:10]
#print(year)  # => 2022
#
##name[начальный индекс:конечный индекс]
#
#day = date[0:2] # => 18
#month = date[3:5] # => 12
#print(day)
#print(month)
#
#print()
#
## Можно и так
#
#Last_name_and_first_name = 'Michael Jordan'
#
#print('Фамилия: ' + Last_name_and_first_name[0:7]) # => Michael
#print('Имя: ' + Last_name_and_first_name[8:14]) # => Jordan
#
#print()
#
##или так
#
#Last_name_and_first_name2 = 'Mike Tyson'
#
#print('Фамилия: ' + Last_name_and_first_name2[:4]) # => Mike
#print('Имя: ' + Last_name_and_first_name2[5:]) # => Tyson
#
#print()
#
#football = 'Argentina' # Qatar World Cup 2022 / ⁡⁣⁢⁣Argentina Champion⁡
#
#print(football[5:-1]) # => tin
#print(football[-7:5]) # => gen
#print(football[0:-4]) # => Argen
#print(football[0:6:2]) # =>Agn  /  0:6 => Argent :2 каждая второя  => Agn
#print(football[:9:2]) # => Agnia / каждую вторую букву
#print(football[2::3]) # => gta / I'm surprised myself
#print(football[4:0:-1])# => negr   = > I'm not racist
#print(football[::-1]) # anitnegrA
#print(football[::1]) # Argentina
#
#
#print()
#
## ⁡⁢⁣⁢Если мы хотим подсчитать сколько букв или символов в переменном мы use len()⁡
#
#Song = 'Phonk' # => 5
#numbers ='123456' # => 6
#numbers2='123456 7' # => 8 потому что там есть пробел
#
#print(len(Song))
#print(len(numbers))
#print(len(numbers2))
#
#print()
#
## можно так
#Song2 = 'Classic'
#print(len(numbers2) -1) # => 7 думаю вы уже догадались почему 7
#print(f'Последний символ: {Song[len(Song) - 1]}') # => k
#print(f'Последний символ: {Song2[len(Song) - 1]}') # => s
## Подумате почему так ...
## ⁡⁣⁢⁣Условие становится ищё сложнее⁡⁡
## ⁡⁣⁢⁣Как вы увидите дальше, выражения можно комбинировать,⁡
## ⁡⁣⁢⁣получая все более сложное поведение в разных местах и любым образом.⁡
##⁡⁣⁢⁣ Чем глубже вы будете изучать Python и практиковаться в нем, тем лучше вы будете понимать ⁡⁣⁢⁣работу с выражениями.⁡
## ⁡⁣⁢⁣Со временем вы поймете, как соединять части кода, чтобы получить нужный результат.⁡
#
#Song3 = "Think I'm joking When I'm talking About blowing my hed open"
#print(f'First: {Song3[0]}\nLast: {Song3[-1]}')
##First: T
##Last: n
#
#print()
## ⁡⁢⁣⁡⁢⁣⁣by the way , если нам данно две переменых типа имя и фамилия и мы должны их сложить в одну строку то это делаем так⁡
## ⁡⁢⁣⁢за одно посмотрим что делает title() and capitalize()⁡
#
#na  = "michael".capitalize() #They dont'tcare about us
#su  = "jackson".capitalize() #Beat it
#
#n  ="jim carry".title()
#s  ="sylvester stallone ".title()
#f  ="megan fox".capitalize()
#
#
#print(n) # => Jim Carry
#print(s) # => Sylvester Stallone
#print(f) # => Megan fox
#
#
#print(na , su )
#print(na +'', su )
#print(f'{na} {su}')
#print('{} {}'.format(na, su )) # => Michael Jackson
## надеюсь вы поняли
#
#print()
#
## ⁡⁢⁣⁢lower /find /replace⁡
#
#moon = 'Python'
#
#print(moon.upper()) # => PYTHON верхний регистр
#
#print(moon.lower()) # => pyhton нижний регистр
#
#print(moon.find('h')) # => 3 поиск и ответ
#
#print (moon.replace('thon', 'fish')) # => Pyfish заменяет
#
#print()
#
## ⁡⁢⁣⁢Всего в Python есть 4 базовых типа данных / переменных:⁡
#
## 1 = ⁡⁢⁣⁢Integer⁡ - целые числа;
## 1.12 = ⁡⁢⁣⁢Float⁡ - числа с плавающей точкой;
## "Привет" = ⁡⁢⁣⁢String⁡ - строки;
## True = ⁡⁢⁣⁢Boolean⁡ - тип данных принимающий либо False, либо True.
#
#number1 = 2022
#number2 = 88
#result = number1 + number2
#result2 = result + 890 # 3000 = 2110 + 890
#print(number1 + number2) # 1) 2022 + 88 = 2110 you think answer 2100 ha-ha-ha ( women ( coffee ) )
#
#print()
#
##print(result) Answer 2110
#
#print(result2) # 2) do you get it ? of course , it's easy
#
#print()
#
## Можно ещё так
#print ( 70 * (3 + 5) / (9 - 2) ) # 3+5=8, 9-2=7, 70*8=560, 560/7=80 { 80.0 }
#
## при делениий если мы хотим увидет числот без плаваюшей точки мы можем use { // } or int
#print(560//7 ) # => 80
#
## ищё есть { % } в python нам показывают не сам процент от цисла а остатот от цисла к примеру
#print(243 % 3) # => 0 остаток
#print(215 % 15) # => 5 остаток
#
#print()
#
## ⁡⁢⁣⁣Мы ещё можем вводить числа в number1 and number2⁡
## ⁡⁢⁣⁢Для этого используем input а  int ( Integer ) преобразует в целые числа⁡
#
#numb1 = int (input ("number1 ")) # вводим первое число
#numb2 = int (input ("number2 ")) # вводим второе число
#res = numb1 + numb2 # { + }
#print(res) # By the way , print это типа итога , он активирует код
#
#print()
#
## Не только { + } но и другие операций { - } { * } { / }
#
#num1 = int (input ("number1 ")) # вводим первое число
#num2 = int (input ("number2 ")) # вводим второе число
#print(num1 - num2)
#
#print()
#
## ⁡⁢⁣⁢есть ещё float числа с плавающей точкой ( это типа десятичное число ) ну типа 10.5 + 1.5 = 12.0⁡
#
#nu1 = float ( input ("number1 ")) # вводим первое число
#nu2 = float ( input ("number2 ")) # вводим второе число
#
#print (nu1 + nu2)  #{ + }
#print(nu1 - nu2)   #{ - }
#print (nu1 * nu2) #{ * }
#print(nu1 / nu2)  #{ / }
#
#print()

## ⁡⁢⁣⁢Если мы хотим округлить мы use round()⁡
#
#ph = 10.6245
#
#print(round(ph, 0)) # => 11.0  =>второе число это команда коду до чего округлять ...
#print(round(ph, 1)) # => 10.6
#print(round(ph, 2)) # => 10.62
#
#print()
#
##и что бы сделать степень мы use { ** }
#
#n1 = int( input ( "number1 ")) # вводим первое число
#n2 = int( input ("number2 "))# вводим второе число
#
#print ( n1 ** n2)
#print(pow(n1, n2)) # в степен можно ищё с командой pow()
#print(pow(2, 3)) # => 8
#
## ну или так
#print( n1.__pow__(n2))
#
#print()
#
## ⁡⁢⁣⁢а если отрицательное число превратить в положительно ну типа модул { 𝗮𝗯𝘀 }⁡
#print(abs (-78)) # => 78
## ну или так
#Abs = -23
#
#print(Abs.__abs__()) # => 23
#а можно сделать  отрицательным число , без проблем
#print(-abs(99)) # => -99
#print()
#
##что-бы написать текс в коде мы можем исползовать print (" Hello ")
#
#print("Code")
## или  str  ( String )
#print (str("Hello "))
#
#
## ⁡⁢⁣⁢на вверхнем коде мы складывали или вычитали числа , ЕСЛИ мы хотим + числа с текстом мы не можем так ...⁡
##text = "Hey "
##number = 123456
##print ( text + number)  у нас выйдет Error: etc.
## ⁡⁢⁣⁢Мы должны use str > что бы превратить int в str⁡
#
#print (str( 266 ) + " Маршрутка " ) # str у нас должен быть цифрой и текс мы можем писать в " "
#
#print()
#
#text = " abc"
#number = 123
#print (str(number)+ text)
#
#print()
#
#"Magic"
#
#w = 12345
#e = 654321
#
#print(w+e) # 666666
#
#print()
#
## ⁡⁢⁣⁢Lesson 3 /⁡⁢⁣⁢True and False type Bool⁡⁡
## ⁡⁢⁣⁢Истина или Ложь Булевой тип значение⁡
#
#
#a = 5
#b = 10
#print ( a == b) # False
#
#
#c = 3
#d = 6 - 3
#print (c == d) # True
#
#
#q = 5 > 10
#print (q) # False
#
#print()
#
#print(3==3) # True
#print(3==5) # False
#print(4!=5) # True /  4 не ровно 5
#print(5>=9) # False
#print(5 > 9 or 5 == 9 )
## не забываем что or будет показывать true если одна из вариантов верна а другая нет
#print(3<=7) # True
#print(2>-3 and 5<8) # True / and будет считывать оба варианта
#print(3<7 and 9<4) # False / если один вариант будут неправильным будут False
#
#print()
#
#name2 ='Bektur'
#print(name2.startswith('B')) # True проверяет первую букву , если мы введем 'b' будет False
#
#print(name2.endswith('r')) # True  проверяет последнию букву
#
#print(name2.isdigit()) # проверяет цивры в name2  /должны быть все цивры / False
#
#print(name2.isalpha()) # проверяет буквы /  False
#
#print()
#
#
#login = 'Bob123'
#print ( input ( 'login ') == login ) # Здесь мы должны ввести логин Bob123 ответ выйдет # True
## Если мы введем не тот логин который нам задан то это будут # False
#
#print()
#
#x = ( input ("number_1 ")) #вводим первое число
#y = ( input ("number_2 ")) #вводим второе число
#
#print ( x < y )  # if x < y это True if not False
#print ( x > y )  # if x > y это True if not False
#print ( x == y ) # if x = y это True if not False
#
#print()
#
#print( int ( True )) # 1
#print ( int ( False )) # 2
#print ( bool ( 1 )) # True
#print ( bool ( 0 )) # False
#
#print()
#
## Тут если говорить человеческим и логическим языком то значение { 0 } это всегда False, нут результата , нет значение
## а любой другой результат { 1,2,3,4,5,6...} дают нам True , есть результат, есть значение
#
#print ( bool (0.00000000001)) # даже если такое число то выйдет True потому что есть рузультат > 0
#
#print ( bool ( )) # False , because empty string is the not result  { 0 } Without { '' } / { "" }
#
#print ( bool ( ' ' )) # True  , because a space/empty string is the result > 0
#print ( bool ( " " )) # True
#
#print()
#
## ⁡⁢⁣ max , min ну это легкая тема ⁡
#
#mx = max (2, 5 , 9, 7)
#mn = min (9, 4, -2, 1)
#
#print(mx) # => 9
#print(mn) # => -2
#
#print()
#
## ⁡⁢⁣⁢Lesson 4 / Библиотеки - это файлы с шаблонами кода. что бы упростить работы ,⁡
## ⁡⁢⁣⁢что бы вы не писали один и тот же код нескольоко раз.⁡
## Библиотек в Python тысячи значить и тысячи разных функий , запомнить все это очень сложно.
## Но мы должны занть основы , этого достаточно для начало ,
## со временен и работой с этим мы станете опытнее и начнете use другие функици или эфективно use их .
#
## К примеру команда type() определяет тип данного аргумента , тип данных
#
#print(type('TEXT')) # => < class 'str'>
#print(type(2022)) # => < class 'int' >
#print(type(6.4)) # => < class 'float' >
#print(type(True)) # => < class 'bool' >
#
## and
#
#print(type({"google",17})) # set => set => набор
#
#get = ("fuel", "doom" ,  314, 34.3)
#print(type(get)) # tuple => кортеж , его нельзя изменит , потому что оно устойчивое выражения , ну типа факт
#
#get2 = "dgsdf" , "gsrg" , 22, 23.5 , True , False
#
##get2 = list(get2)
## но если нужно изменит кортеж то вот так
##get2 = set(get2)
#
#get3 = ["qwerty", "ytrewq", 23.3 , 5]
#print(type(get3)) # list => Список
#
#print(["fsedgz", 34]) # list
#print(list('Python')) # => 'P', 'y', 't', 'h', 'o', 'n'
#
#get4 = ['Сергей', 'Мария', 'Антон']
#print(get4)
#
#print(get4) # =>'Сергей', 'Саша', 'Антон'
#
#print(get4[-1])# => 'Антон'
#


#get5 = [23, 4.6, 'code', True]
##get6=get5
###get6.reverse()
#print(get5)
##способы добавление в список
#
##get5.append(312)
#get5.insert(2, 'python')
##get5.extend(get4)
##get5 += get3
#print(get5)
##изменение

#get5[3], get5[2] = get5[2], get5[3]
#get5[0] /2 , *2 , ...
#get5[3] = False
#get5[0, 1] = [False]
#get5[2] = get5[get5.index('code')].replace('c', '')
#get5[2] = get[2].replace('c', '')
#get5.reverse()

#get6 = [ 12, 4.6, 59.3, 6, False, 1]
#get6.sort()
#get6.sort(reverse=True)
#get6 = ['tesla', 'amazon', 'facebook', 'apple']
#get6.sort()
#get6.sort(key=len)
#print(get6)


#удаление

#get5.remove(4.6)
#get5.pop(3)  / 'переменная' = get5.pop(3) => True
#del get5[1:4]
#get5 = [i for i in get5 if i != 4.6]

#print(get5)

#copy
#
#a = ['true', 'город312', 'cdm', 'home', 'false']
#
#b = a.copy()
#
#c = a
#c[1] = 'Москва'
#
#print(b is a) #False
#print(id(b), id(a))
#
#print(c is a ) #True
#print(id(c), id(a))
#
#print(a)
#print(b)
#print(c)
#
##⁡⁢⁣⁢ Lesson 5 :  if / elif / else { +/- }⁡
#
#
#po = 0
#
#
#if po == 0 :
#    po += 1 # => 0 + 1 = 1
#
#print(6/po) # => 6 , 6 / 1 = 6
#
## если написать другое число , к примеру 2 , у нас po не проходить проверку if
## и у нас этот код не работает и переходит к другому
#
#po2 = 2
#
#if po2 == 0:
#    po2 +=1
#
#print(6/po2) # => 6 / 2 = 3
#
## Код читается сверху вниз / слева на право
#
#po3 = 0 # из-за того что у нас x равен нулю у нас выходит if
#
#
#if po3 == 0 :
#    print('if')
#
## если x был бы больше нуля то выходило бы elif
#
#elif po3 > 0 :
#    print('elif')
#
## а если он не проходит ни одну проверку то работает else
#
#else :
#    print('else')
#
#po4 = int and float (input())
#
#if po4 == 0 :
#    print("po4 = 0 ")
#
#elif po4 < 0 :
#    print("po4 < 0")
#
#elif po4 > 0 :
#    print("po4 > 0")
#
#print()
#
#sm = ''
#
#if sm == 'Sun' or sm == 'Солнце':
#    print('Day')
#
#elif sm == 'Moon' or sm =='Ночь':
#    print('Night')
#
#else :
#    print("Day or Night , I don't Know Bro")
#
#
#print()
#
#ul = 3
#
#if ul == 0:
#    ul = 1
#    print('ul был равен нулю ) ul = 1')
#
#elif type (ul) == type(9) or type (ul) == type(9.9):
#    print('ul допустимы тип данных')
#
#else:
#    print('ul недопустимый тип данных')
#
#
#print(100/ul)
#
## in он проверяет есть ли в правом тексте символы как в левом , если да то мы уви
#
#print("Ok" in " are you Ok") # => True
#
#love = "you" in "I love you"
#
#if love == True:
#    print("You :)")
#
#print()
#
#password = input("Придусайте пароль состоящийся из 6 или более символов ")
#
#if  len (password) >= 6:
#    print("all Ok ")
#
#else:
#    print("пароль не подходит , придумайте другой ")
#
#print()
#a=int(input("Введите число А: "))
#b=int(input("Введите число В: "))
#if a%b == 0:
#    print("YES")
#else:
#    print("NO")
## ⁡⁢⁣⁢Lesson 6 Циклы   while , for ⁡
#
#wi = 0
#while True:
#    print("Hello")
#    wi += 1
#    if wi  == 3:
#        break # останавливает цикл
#
#
##⁡⁢⁣⁢ ‍while это команда которая будут бесконечна работать если его не остановать командай break⁡
#
#print('\n')
#
##  можно остановить while и другими способами
#
#wi2  = 0
#while wi2 != 3 : # тут мы указываем команду что c не должна быть 4 и мы увидем 4 слов World потому что у нас s начинается с 0
#    print("World")
#    wi2 += 1
#
#print('\n')
#
#wi3 = 0
#while wi3 != 12:
#    #print (wi3)
#    wi3 += 1
#    if wi3 == 9 :
#        print("Nine nine nine = 9")
#        continue # продолжать / перерывать/ пропускать
#    print(wi3)
#
#print('\n')
#
## обратный отсчет
#
#wi4 = 10
#while wi4 != 0 :
#    print(wi4)
#    wi4 -= 1
#
#print('\n')
#
## факториял n!
#
#while True :
#    wi5 = int(input(">"))
#    wi6 = 0
#    wi7 = 1
#
#    while wi6 < wi5 :
#        wi6 += 1
#        wi7 *= wi6
#        #print(wi6)
#
#    else:
#        print(wi7)
#        break
#
#print('\n')
#
#
## ⁡⁢⁣⁢𝗳𝗼𝗿 переберает данные , обьекты⁡
#
#word = 'Python'
#
#for let in word:
#    print(let) # P y t h o n / повертикали
#
#print()
#
#for let in word:
#    print(let, end='') # Python
#
#print()
#
#for let in word :
#    print(f'{let} - {word.index(let)}') #index
#
#
#print()
#
#wi8 = 1
#for let in word:
#    print(f'{let} - {wi8}')
#    wi8 += 1
#
#print()
#
#wi8 = 1
#for let in word:
#    print(f'{let} - {wi8}')
#    wi8 += 1
#    if let == 'y':
#        break
#
#print()
#
#wi8 = 1
#for let in word:
#    if let == 'h':
#        continue
#    print(f'{let} - {wi8}')
#    wi8 += 1
#
#print()
#
#for f in range(1,6): # ⁡⁢⁣⁢range это последовательность чисел⁡
#    print(f*f)
#
#print()
#
#for r in range (1,6):
#    for p in range (1,4):
#        print(f'r {r} - p {p}')
#
#print()
#
#wi9 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#xi = input ("Text:\n")
#
#for i in wi9:
#    count = 0
#    for r in xi :
#        if i == r:
#            count += 1
#    if count > 0 :
#        print('Букв', i, 'было', count)
#
#print()
#
#english = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
#russion = "йцукенгшщзхъфывапролджэячсмитьбю"
#
#while True:
#    inp =input("\nВвод слов: ")
#    for i in inp :
#        if i in english:
#            print(russion[english.index(i)], end='')
#        else:
#            print(english[russion.index(i)], end='')
#
#
#
#print()
#
#
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#for number_1 in numbers:
#    for number_2 in numbers:
#        print(number_1, '*', number_2, '=', number_1 * number_2)
### ​‌‍‌⁡⁣⁢⁣Угадай что будет с этоим кодом⁡​
#

#⁡⁢⁣⁢ Если нужно пройтись по списку или по диапазону чисел в обратном порядке — вызывайте функцию reversed()⁡
#
#for i in reversed(range(1, 6)):
#    print(i, 'бомм!')
#
#print('C новым годом!')

# ⁡⁢⁣⁢Lesson 7 / Объявление функции  def ⁡⁢⁣⁢, Словари и Множества ⁡

#def hello ():
#    print("How are you?")
#
#print("Hello")
#
#hello()
#
#
#
#def hello(name):
#    print('Hello ' + name )
#
#hello('Jonh')
#hello('Anna')
#hello('Bitch')


#def hello(name, thing):
#    print(name + ', приветствую тебя! Держи ' + thing)
#
#hello('Сергей','трусы')


#
#
#def _home(name='Инкогнито', planet='Икс'):
#    print(name + ' живёт на планете ' + planet)
#
#
#_home('Босс')
#
#
#def home(name='Инкогнито', planet='Икс'):
#    print(name + ' живёт на планете ' + planet)
#
#home(planet='Земля')
#home(planet='Земля', name='Винни Пух')
#playlist = {
#    'Venus',
#    'Yesterday',
#    'Fireball',
#    'Time',
#    'Poison'
#}
#cities = [
#    'Вологда',
#    'Чебоксары',
#    'Тольятти',
#    'Москва',
#    'Бремен',
#    'Санкт-Петербург',
#    'Новороссийск',
#    'Челябинск',
#    'Вологда',
#    'Новосибирск',
#    'Челябинск',
#    'Санкт-Петербург',
#    'Москва',
#    'Новосибирск'
#]
#
#unique_cities = set(cities)
#
#for i in unique_cities:
#    print(f'- {i}')
#
#
#
#
#
#

#playlist.add('Thunderstruck') # add() чтобы добавить новый элемент к множеству
#print(playlist)
## Будет напечатано:
## {'Yesterday', 'Fireball', 'Thunderstruck', 'Poison', 'Venus', 'Time'}
## Элементы множеств никогда не соблюдают порядок!
#
#playlist_1 = {'Три белых коня', 'Happy new year', 'Снежинка'}
#playlist_2 = {'Last christmas', 'Снежинка', 'Happy new year'}
#playlist_3 = playlist_1.union(playlist_2)    #union() объединяет множества
#
#print(playlist_3)
#

#
#def print_valid_cities(a, b):
#    diff = all_cities.difference(used_cities)
#    for city in diff:
#        print(city)
#    # Вместо этого многоточия напишите код функции, она должна
#    # принимать и обрабатывать аргументы all_cities и used_cities,
#    # а затем печатать результат в нужном формате
#
#all_cities = {
#    'Абакан',
#    'Астрахань',
#    'Бобруйск',
#    'Калуга',
#    'Караганда',
#    'Кострома',
#    'Липецк',
#    'Новосибирск'
#}
#
#used_cities = {'Калуга', 'Абакан' , 'Новосибирск'}
#
#print_valid_cities(all_cities, used_cities)
##
#def get_together_games(games_1, games_2):
#    # Напишите здесь код функции для поиска пересечений
#        #return together_games
#        return set(games_1).intersection(set(games_2)) # intersection() типа поисковик
#
#anfisa_games = [
#    'Online-chess',
#    'Города',
#    'DOOM',
#    'Крестики-нолики'
#]
#alisa_games = [
#    'DOOM',
#    'Online-chess',
#    'Города',
#    'GTA',
#    'World of tanks'
#]
## Вызовите функцию со списками игр в качестве параметров
#together_games = get_together_games(anfisa_games, alisa_games)
## Напечатайте итоговый перечень игр в цикле
#for i in together_games:
#    print(f'👾 {i}')
#
##Задача 3
##Бот Анфиса и бот Алиса хотят сыграть во что-нибудь по сети. Каждая из них составила список игр, в которые она умеет играть. Списки, к
##Вам нужно написать программу, которая найдёт одинаковые элементы в двух списках.
##
#dump = {
#    1: 'единица',               # Ключ - число, значение - строка.
#    'земляника': 'ягода',       # И ключ, и значение - строки.
#    'помидор': 'ягода',         # Значение 'ягода' - не уникально. Так можно.
#    False: 0,                   # Ключ - булево значение, значение - число.
#    'лук': ['овощ', 'оружие'],  # Ключ - строка, значение - список.
#                                # Ключ - строка, а значение - словарь. Так тоже можно!
#    'англо-русский словарь': {'рука': 'hand',
#                              'нога': 'leg',
#                              'бэкенд-разработчик': 'back-end developer'
#                               },
#}
#
#print(dump['лук'])
## Будет напечатано ['овощ', 'оружие']
#
#english = {
#    'рука': 'hand',
#	'нога': 'leg',
#    'хвост': 'tail',
#    'питон': 'python',
#	'бэкенд-разработчик': 'back-end developer'
#}
#
## Элементу с ключом 'рука' присвоим новое значение
#english['рука'] = 'arm'
#
#print(english['рука'])
##
#english = {
#    'рука': 'arm',
#    'нога': 'leg',
#    'хвост': 'tail',
#    'питон': 'python',
#    'бэкенд-разработчик': 'back-end developer'
#}
#
## Создаём новый элемент словаря через доступ по ключу
#english['голова'] = 'head'
## если вызван ключ, которого нет в словаре — будет создан новый элемент словаря.
#print(english['голова'])
#
#
#У словарей есть метод update(), он позволяет объединить два словаря, то есть добавить в один словарь элементы другого.
#english = {
#    'рука': 'arm',
#    'нога': 'leg',
#    'хвост': 'tail',
#    'питон': 'python',
#    'бэкенд-разработчик': 'back-end developer',
#    'голова': 'head'
#}
#
## Объявим новый словарь
#new_words = {'мозг': 'brain', 'логика': 'logic'}
#
## Добавим в словарь english элементы словаря new_words
#english.update(new_words)
#1w3r5y7i9p0
#code1python
## Посмотрим, что теперь хранится в словаре english
#print(english)
#
## Заодно выясним, что произошло со словарём new_words
#print(new_words)
#

#Значения всех ключей можно извлечь из словаря и собрать в одну коллекцию. Для этого у словаря есть метод values():
# Словарь, в котором хранятся начертания букв и их названия
#old_letters = {
#    'Богатый': 'Б',
#    'Образованный': 'О',
#    'Местный': 'М',
#    'Житель': 'Ж'}
#
#print(old_letters.values())
## Будет напечатан список значений словаря
## dict_values(['Б', 'О', 'М', 'Ж'])
#
#Подобным образом можно получить и коллекцию ключей словаря, для этого есть метод keys():
#
#favorite_songs = {
#    'Тополиный пух': 'Иванушки international',
#    'Город золотой': 'Аквариум',
#    'Звезда по имени Солнце': 'Кино'
#}
#
#print(favorite_songs.keys())
## Будет напечатан список ключей словаря
## dict_keys(['Тополиный пух', 'Город золотой', 'Звезда по имени Солнце'])

#
#english = {
#    'рука': 'hand',
#    'нога': 'leg',
#    'хвост': 'tail',
#    'питон': 'python',
#    'бэкенд-разработчик': 'back-end developer'
#}
## Собираем ключи словаря в коллекцию
## и преобразуем эту коллекцию в список
#words_ru = list(english.keys())
#
## Собираем значения словаря в коллекцию
## и преобразуем эту коллекцию в список
#words_en = list(english.values())
#
## Печатаем списки
#print(words_ru)
#
#print(words_en)

#
#friends =  {
#    'Серёга': 'Оренбург',
#    'Соня': 'Москва',
#    'Миша': 'Москва',
#    'Дима': 'Челябинск',
#    'Алина': 'Красноярск',
#    'Егор': 'Пермь',
#    'Коля': 'Красноярск'
#}
#
## Здесь ваш код
#
#a = set(friends.values())
#
#for i in a:
#      print(i)
#
#favorite_songs = {
#    'Тополиный пух': 'Иванушки international',
#    'Город золотой': 'Аквариум',
#    'Звезда по имени Солнце': 'Кино',
#    'Space Oddity': 'David Bowie',
#    'Рыба': 'Аквариум',
#    'Серенада Трубадура': 'Муслим Магомаев',
#}
#
#for song, performer in favorite_songs.items():
#	print('Песню ' + song + ' исполняет ' + performer)
#ключ и значение
#favorite_songs = {
#    'Тополиный пух': 'Иванушки international',
#    'Город золотой': 'Аквариум',
#    'Звезда по имени Солнце': 'Кино',
#    'Space Oddity': 'David Bowie',
#    'Рыба': 'Аквариум',
#    'Серенада Трубадура': 'Муслим Магомаев',
#}
## Извлечём и напечатаем только значения (values) каждого элемента
#for singer in favorite_songs.values():
#	print('Доктор, я больше не могу слушать исполнителя ' + singer)
#
## А в этом цикле извлечём и напечатаем только ключи (keys) словаря
#for music in favorite_songs.keys():
#	print('Доктор, я каждый день по три раза слушаю песню ' + music)
#
#friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
#friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']
#
## Объявлен пустой словарь, его нужно будет наполнить элементами,
## каждый из которых составлен по схеме "имя: город"
#friends =  {}
#
## Допишите ваш код сюда
#for i in range(len(friends_names)):
#    friends[friends_names[i]] = friends_cities[i]
#
#
#print("Лена живёт в городе", friends['Лена'])
#
#friends =  {
#    'Серёга': 'Омск',
#    'Соня': 'Москва',
#    'Дима': 'Челябинск',
#    'Айгуль': 'Казань',
#    'Алёна': 'Белгород',
#    'Даниил': 'Санкт-Петербург',
#    'Лев': 'Тула',
#    'Валера': 'Сыктывкар',
#    'Антон': 'Ялта',
#    'Карен': 'Краснодар'
#}
#
## Здесь ваш код
#for key, value in friends.items():
#    print(f'{key} живёт в городе {value}')
#
#
#friends = {
#    'Серёга': 'Омск',
#    'Соня': 'Москва',
#    'Дима': 'Челябинск',
#    'Алина': 'Хабаровск',
#    'Егор': 'Пермь'
#}
#
#def is_anyone_in(collection, city):
#    for collection, city in friends.items():
#            if city =='Хабаровск':
#                print(f'В городе {city} живёт {collection}. Обязательно зайду в гости!')
#            else:
#                print(f'В городе {city} у меня есть друг, но мне туда не надо.')
#
#is_anyone_in(friends, 'Хабаровск')
#
#Можно и так вывести словарь
#a = dict(name='Anton', age='23')
#print(a)
#
### распаковка
#b = dict([[0, 'zero'],[1, 'one'],[2, 'two'],[3, 'three'],[4, 'four'],[5, 'five'],[6, 'six'],[7, 'seven']])
##print(b)
#for i in b :
#    print(f'{i} {b[i]}')
#c = dict(enumerate('python'))
#print(c)





#DATABASE = {
#    'Серёга': 'Омск',
#    'Соня': 'Москва',
#    'Миша': 'Москва',
#    'Дима': 'Челябинск',
#    'Алина': 'Красноярск',
#    'Егор': 'Пермь',
#    'Коля': 'Красноярск'
#}
#
#def process_anfisa(query):
#    if query == 'Сколько у меня друзей?':
#        count = len(DATABASE)
#        return 'У тебя ' + str(count) + ' друзей.'
#    # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
#    elif query =='Кто все мои друзья?':
#        friends_string = ''
#        # Чтобы получить перечень друзей -
#        # переберите словарь DATABASE в цикле
#        for i in DATABASE:
#            friends_string += i + ' '
#
#                  # Добавляйте к переменной friends_string имя друга и пробел
#        # Верните строку, составленную из 'Твои друзья: ' и friends_string
#        return 'Твои друзья: ' + friends_string
#    elif query == 'Где все мои друзья?':
#        city = ''
#        a = set(DATABASE.values())
#        for i in a:
#            city += i + ' '
#
#        return 'Твои друзья в городах: ' + city
#    else:
#        return '<неизвестный запрос>'
#
## Не изменяйте следующий код
#print('Привет, я Анфиса!')
#print(process_anfisa('Сколько у меня друзей?'))
#print(process_anfisa('Кто все мои друзья?'))
#print(process_anfisa('Где все мои друзья?'))
#
#
#numbers = [i for i in range(1,7)]
#numbers_2 = {i: i*i for i in numbers}
#
#print(numbers, numbers_2, sep='\n')
#
#name = ['Anton', 'Alex', 'Jony', 'Adam']
#age = [23, 12, 35, 19]
#
#date = dict(zip(name, age))
#print(date)
#
#date = {}
#a = 0
#
#while a != len(age):
#    date[name[a]] = age[a]
#    a += 1
#
#print(date)
#
#string = 'Я памятник себе воздвиг нерукотворный'
#
#index = [0, 1, 2, 8, 6, 17, 24]
#
#for i in index:
#
#
#    print(string[i], end='')
#
#poem_str = 'I hate YOU'
#
## Применяем к строке метод split(), в скобках указываем пробел в кавычках:
#words_list = poem_str.split(' ')
## Печатаем результат:
#words_list[1] = 'love'
#
#print(words_list)
##
#a ={'мясо', 'лук', 'баран', 'масло'}
#b ={'лук','соус', 'баран', 'томат', 'мясо'}
#print(a.intersection(b))
#print(a & b)
#print(a.difference(b))
#print(a - b )
#print(a.union(b))
#print(a | b)
#print(a.symmetric_difference(b))
#print(a ^ b )
#


#import socket
#hostname = socket.gethostname()
#IPAddr = socket.gethostbyname(hostname)
#print(IPAddr)
#
#import random
#import string
#
#chars = "qwertyuiopasdfghjklzxcvbnm"
#charsl = "QWERTYUIOPASDFGHJKLZXCVBNM"
#numbers = "0123456789"
##symbols = "!@#$%^&*()_-+=[]{ } \ | / ;: ,.<> ? *"
#all = chars + charsl + numbers #+ symbols
#
#password = ''.join(random.choice(all) for i in range(12))
#
#print(password)
#
#from turtle import *
#
#pensize(10)
#
#while 1:
#    forward(2)
#
#    right(5)
#
#exitonclick()
#
# import time
#
# a = 0
#
# while 1 :
    # a += 1
    # print(a)
    # time.sleep(1)
    # if a == 10 :
        # break

        # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number_1 in numbers:
    # for number_2 in numbers:
        # print(number_1, '*', number_2, '=', number_1 * number_2)


# import time
#
# a = 0
#
# while 1 :
    # a += 1
    # print(a)
    # time.sleep(1)
    # if a == 10 :
        # break
#
#
#a = ["beg", "life", "i", "to"]
#word = []
#num = []
#o = {}
#for i in a:
#    b = len(i)
#    word.append(i)
#    num.append(b)
#
#print(word)
#print(sorted(num))
#
#for word, num in o.items():
#    print(sorted(num))
#
# def romanToInt(s):
    # """
    # :type s: str
    # :rtype: int
    # """
    # romannumber = {
        # 'I' : 1,
        # 'V' : 5,
        # 'IV' : 4,
        # 'IX' : 9,
        # 'X' : 10,
        # 'XL': 40,
        # 'L' : 50,
        # 'XC': 90,
        # 'C': 100,
        # 'CD' : 400,
        # 'D' : 500,
        # 'CM': 900,
        # 'M' : 1000
    # }
    # num = 0
    # i = 0
    # while i < len(s):
        # if i + 1 < len(s) and s[i:i+2] in romannumber:
            # num += romannumber[s[i:i+2]]
            # i += 2
        # else:
            # num += romannumber[s[i]]
            # i += 1
#
    # return num
#
# print(romanToInt('XLIII'))
#
#
# x = 150 * ( 20_000_000 / 500) # how output : 6_000_000.0
# print(x)
#
#
# result = 150 * (20_000_000 / 500)
# print(f"{result:,.1f}".replace(',', '_'))
#
#
#
# menu = {
    # 'plov': {'rice', 'meat', 'carrot'},
    # 'manty': {'meat', 'dough', 'onion'},
    # 'pizza': {'cheese', 'dough', 'tomato'},
    # 'okroshka': {'kefir', 'sausage', 'cucumber', 'eggs'},
    # 'rolls': {'fish', 'rice', 'nori'}
# }
#
# while True:
    # word = set(input('>> ').lower().split())
    # if word == 'exit':
        # break
#
    # for key, value in menu.items():
        # if word.issubset(value):
            # print(key)
#
#
# def sum1 (num):
    # counter = 0
    # for i in num:
        # counter += i
    # return counter
#
# print(sum1([1,2,3,4,5,6,7,8,9]))
#
#
#
# def max1 (num):
    # max_num = num[0]
    # for i in num[1::]:
        # if max_num < i :
            # max_num = i
    # return max_num
#
# print(max1([1,2,3,4,5,6]))
#
#
# def min1 (num):
    # min_num = num[0]
    # for i in num[1::]:
        # if i < min_num :
            # min_num = i
    # return min_num
#
#
# print(min1([67,12,43,2,5]))
#
#

# a = 'Hello'
# b = 0
# for i in a:
    # b += 1
#
# print(b)
# print(len('Hello'))
#
# def len1(items):
    # counter = 0
    # for _ in items:
        # counter += 1
    # return counter
#
# print(len1('aplles'))
#
#
# def get_square (a, b):
    # return a * b
#
# q = get_square(10, 24)
# r = get_square(9, 23)
#
# print(q, r,  sep='\n')
#




#
#
#plov = {'rice', 'meat', 'carrot'}
#manty = {'meat', 'dough', 'onion'}
##
#print(plov.difference(manty))
#print(plov - manty)
##
#print(plov.intersection(manty))
#print(plov & manty)
##
#print(plov.union(manty))
#print(plov | manty)
##
#print(plov.symmetric_difference(manty))
#print(plov ^ manty)
#
# def num (a=[1,2,2,2,2,3], b=[2]):
    # ab = set(a)
    # if b[0] in ab:
        # ab.remove(b)
    # return list(ab)
#
#
# print(num())

#
# def num(a=[1, 2, 2], b=[2]):
    # for i in b:
        # if i in a:
            # a.remove(i)
    # return list(a)
#
# print(num())
#
# def num(a=[1, 2, 2], b=[2]):
    # a = [item for item in a if item not in b]
    # return a
#
# print(num())
#
# x = {1: 'Bogdan', 2: 'Alisa'}
# y = {3: 'Alex', 4: 'Margo'}
#
#d = x | y
#
#print(d)
# print(x | y)
#
#
