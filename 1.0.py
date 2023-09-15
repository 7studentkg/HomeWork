#⁡⁢⁣⁢1⁡
#print ("⁡⁢⁣⁢Kyrgyzsta⁡⁢⁣⁢n⁡")
#
#moon = 'no'
#while moon == 'no':
#
#    sun = input ("Область >> ")              #⁡⁢⁣⁢Дополнить⁡
#
#    if sun == 'Чуй':
#        print ("Чуй 28 градусов ")
#
#    elif sun == 'Талас':
#        print ("Талас 22 градусов ")
#
#    elif sun == 'Ысык-Куль':
#        print ("Ысык_Куль 30 градусов ")
#
#    elif sun == 'Нарын':
#        print ( "Нарын 15 градусов ")
#
#    elif sun == 'Джалал-Абад':
#        print ( "Джалал-Абад 26 градусов ")
#
#    elif sun == 'Ош':
#        print ("Ош 32 градусов ")
#
#    elif sun == 'Баткен':
#        print ("Баткен 24 градусов")
#    elif sun :
#        print ("Error")
#
#    moon = input ('Завершить ( no ) >> ')


#
#print("Kyrgyzstan")
#
#a = float ( input ("Чуй "))
#b = float ( input ("Талас "))
#c = float ( input ("Ысык-Кол "))
#d = float ( input ("Джалал-Абад "))
#e = float ( input ("Нарын "))
#f = float ( input ("Ош "))
#g = float ( input ("Баткен "))
#
#abc =  ( a + b + c + d + e + f + g) / 7
#
#abc = round (abc, 1 )
#
#print (abc)
#
#
#
#regions = ['Чуй', 'Талас', 'Ысык-Куль', 'Джалал-Абад', 'Нарын', 'Ош', 'Баткен']
#heat = {i: int(input(f'Введите температуру области {i}: ')) for i in regions}
#
#print(round(sum(heat.values()) / len(heat),2))
#
#print("\n")
#
#
#import calendar
#
#print(calendar.TextCalendar().pryear(2023))
#
#
#print('\n')
#
#2
"Задане : Знаки зодиака "

#ay = int(input("День рождения: "))
#onth = int(input("Месяц: "))
#
# ⁡⁣⁢⁣Ввод данных в одну строку⁡
#
# date = (input("Дата рождения:  ")) / 19-8 , 19.8 , 19/08 ...
# day = int(date[0:2:1])
# month = int(date[3:5:1])
#
#day = int(date[0:2:1])
#
#
#f (day >= 21 and day <=31 and month == 3) or (day <=20 and month == 4 ) :
#   print("Знак зодиака: Овен")
#
#lif ( day >= 21 and day <= 30 and month == 4 ) or (day <=21 and month == 5 ) :
#   print("Знак зодиака: Телец")
#
#lif ( day >= 22 and day <= 31 and month == 5) or (day <=21 and month == 6 ):
#   print("Знак зодиака: Близнецы")
#
#lif ( day >= 22 and day <= 30 and month == 6) or (day <= 22 and month == 7 ):
#   print("Знак зодиака: Рак")
#
#lif (day >= 23 and day <= 31 and month == 7) or (day <= 21 and month == 8 ):
#   print("Знак зодиака: Лев")
#
#lif (day >= 22 and day <= 31 and month == 8) or (day <= 23 and month ==9 ):
#   print("Знак зодиака: Дева")
#
#lif (day >= 24 and day <= 30 and month == 9) or (day <= 23 and month == 10 ):
#   print("Знак зодиака: Весы")
#
#lif (day >= 24 and day <= 31 and month == 10) or (day <= 22 and month == 11 ):
#   print("Знак зодиака: Скорпион")
#
#lif (day >= 23 and day <= 30 and month == 11) or (day <= 22 and month ==12 ):
#   print("Знак зодиака: Стрелец")
#
#lif (day >= 23 and day <= 31 and month == 12) or (day <= 20 and month == 1 ):
#   print("Знак зодиака: Козерог")
#
#lif (day >= 21 and day <= 31 and month == 1) or (day <= 19 and month == 2 ):
#   print("Знак зодиака: Водолей")
#
#lif (day >= 20 and day <= 28 and month == 2) or (day <= 20 and month == 3 ):
#   print("Знак зодиака: Рыбы")
#
#lse:
#   print("ERROR BRO\nПример >>\nДень рождения: '19'\nМесяц: '8'\nВыводить> Знак зодиака: 'Лев'")
#
#
#print('\n')


#"Счетчик букв (гл. и согл.)"    #⁡⁢⁣⁢3 ⁡
#
#while True:
#
#    гласные = 0
#    согласные = 0
#
#    word = input("Ввод: ")
#
#    for i in word:
#        k = i.lower()
#
#        if k == "a" or k == "e" or\
#           k == "i" or k == "o" or\
#           k == "u" or k == "y" or\
#           k == 'а' or k == 'о' or\
#           k == 'у' or k == 'ы' or\
#           k == 'е' or k == 'я' or\
#           k == 'э' or k == 'ю' or\
#           k == 'и' or k == 'ё':
#            гласные += 1
#
#        else:
#            согласные += 1
#    if word == 'stop':
#        print("Thanks bro")
#        break
#
#    print("Количество букв "+str(len(word))+'\n'+ "Гласных букв %i\nСогласных букв %i" % (гласные, согласные))
#    print("Гласных: " + str(гласные * 100 / len(word))+'%' + "\n" + "Согласных: " + str(согласные * 100 / len(word)) +'%')
#
#
#
# 2 вариант
#
#all = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm'
#g ='aeiouyауоеёяиюэы'
#
#
#while True:
#
#    gl = 0
#    sogl = 0
#    s = 0
#
#    word= input("Введите слово: ")
#    word2=word
#
#    for i in word.lower():
#        if i in all:
#            s += 1
#            if  i in g:
#                gl+=1
#            else:
#                sogl+=1
#    if word == 'stop':
#        print("Thanks bruh")
#        break
#
#    print(f'Слово:{word2}')
#    print(f'Количество букв:{s}')
#    print(f'Согласных: {sogl}')
#    print(f'Гласных: {gl}')
#    print(f'Процент Гласных: {round(gl / s * 100, 2)}; Процент Согласных: {round(sogl / s * 100, 2)}')
#
#
#3 вариант
#while 1 :
#    word = input('Введите слово : ').lower()
#    if word =='stop':
#        break
#
#    elif word == 'стоп':
#        break
#
#    else:
#        gl ='aeiouyауоеёяийюэы'
#        sl ='qwrtpsdfghjklzxcvbnmцкнгшщзхфвпрлджчсмтб'
#
#        b = 0
#        c = 0
#
#        print(f'Слово: {word}')
#
#        print('Всего символов:', len(word))
#
#        for i in word :
#            if i in gl:
#                b += 1
#        print('Гласных:', int(b))
#
#        for u in word :
#            if u in sl:
#                c += 1
#        print('Cогласных:', int(c))
#
#        Sg = round(b / len(word) * 100, 2)
#        Ss = round(c / len(word) * 100, 2)
#
#        print(f'Процент Гласных: {Sg}%')
#        print(f'Процент Согласных: {Ss}%')
#
# My version
#
# while 1 :
    # word = input("Введите слово: ").lower()
#
    # if word == 'stop' or word == 'стоп':
        # break
#
    # else:
        # gl = 'aeiouyауоеёяийюэы'
#
        # count_gl = 0
        # count_sogl = 0
#
        # print(f'Слово: {word}')
        # print(f'Количество букв: {len(word)}')
#
        # for i in word :
            # if i in gl :
                # count_gl += 1
            # elif i not in gl:
                # count_sogl +=1
#
        # print(f'Гласных: {int(count_gl)}')
        # print(f'Согласных: {int(count_sogl)}')
#
        # print(f'Процент гласных букв в слове: {round(count_gl / len(word) * 100 , 2)}')
        # print(f'Процент согласных букв в слове: {round(count_sogl / len(word) * 100 , 2)}')

# version my students
# while True:
    # name = input('Слово: ')
    # if name == 'stop' or name == 'стоп':
        # print('exit...')
        # break
    # vowels = "аеиуыоэяюaeiouy"
    # consonants = "йцкнгшщзхфвпрлджчсмтбqwrtpsdfghjklzxcvbnm"
    # counter1 = 0
    # counter2 = 0
    # for i in name.lower():
        # if i in vowels:
            # counter1 += 1
        # elif i in consonants:
            # counter2 += 1
        # else:
            # print('Только слова состоящие из алфавита')
    # summ = counter1 + counter2
    # percent1 = round(counter1 / summ*100, 2)
    # percent2 = round(counter2 / summ*100, 2)
    # print(f'Количество букв: {summ} ')
    # print(f'Гласных букв: {counter1}')
    # print(f'Cогласных букв: {counter2}')
    # print(f'Процент гласных букв: {percent1} ')
    # print(f'Процент согласных букв: {percent2} ')
#
#
# ⁡⁢⁣⁢4 ChatGPT⁡
#
#data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')#

#letters, numbers =[], []#

#for i in data_tuple:
#    if isinstance(i, str): # isinstance() - проверяет объект на указаный класс : типа таможня
#        letters.append(i)
#    else:
#        numbers.append(i)#

#numbers.remove(6.13)
#letters.append(numbers.pop(0))#
#

#numbers.insert(2, 2)#

#numbers = [x ** 2 for x in numbers]#

#numbers.sort()
#letters.reverse()#

#letters[1] = 'G'
#letters[-2] = 'c'#

##true= []
##true.append(letters.pop(0))      #перемешение True в конец
##letters += true#

#letters = tuple(letters)
#numbers = tuple(numbers)#
#

#print("letters:",letters) # (True, 'G','e','e','k','T','e','c','h') or ('G','e','e','k','T','e','c','h',True)
#print("numbers:",numbers) # (1, 4, 9)#
#

##2 вариант#

#data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')#

#letters, numbers =[], []#

#for i in data_tuple:
#    letters.append(i) if type(i) == str else numbers.append(i)#

#del numbers[0]
#letters.append(numbers.pop(0))#

#numbers.insert(2, 2)
#numbers = [x ** 2 for x in numbers]#

#numbers.sort()#

#letters[0], letters[-2] = letters[-2], letters[0]
#letters[1], letters[-3] = letters[-3], letters[1]   # голова болит б**
#letters[3], letters[4] = letters[4], letters[3]#

#letters[0] ='G'
#letters[-3] ='c'#

#letters = tuple(letters)
#numbers = tuple(numbers)#

#print("letters:",letters)
#print("numbers:",numbers)#


# ⁡⁢⁣⁢5 ChatGPT Again...     ​‌‍‌𝗿𝗲𝗺𝗮𝗸𝗲​

#
#data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Boiler", "0510", "Phonex", "0543")
##
## 1
#designations = []
#codes = []
##
## 2
#for d in data:
#    if d.isnumeric():
#        codes.append(d)
#    else:
#        designations.append(d)
##
## 3
#operators = {}
#i = 0
#while i < len(designations):
#    operator = designations[i]
#    code = codes[i]
#    if operator not in operators:
#        operators[operator] = set()
#    operators[operator].add(code)
#    i += 1
##
## 4
#del operators["Boiler"]
#del operators["Phonex"]
##
## 5
#operators["O!"].update({"0700", "0500"})
#operators["Megacom"].update({"0999", "0555"})
#operators["Beeline"].update({"0222", "0777"})
##
## 6
#for operator, code_set in operators.items():
#    print(operator, "-", code_set)
#
##
#studens_numbers = {
#    'argen': 1,
#    'baktybek': 2,
#    'vlad': 3,
#    'kutman': 4,
#    'tima': 5
#}
#
#def find_student(name):
#    if name in studens_numbers.keys():
#        return True
#    return False
#
#
#def add(name: str, numbers: int ):
#    #if name not in studens_numbers.keys():
#    if not find_student(name):
#        if numbers in range(1, 6):
#            studens_numbers[name] = numbers
#        else:
#            print('От 1 до 5 ')
#    else:
#        print(f'{name} такое имя есть ')
#
#
#def delete(name):
#    #if name in studens_numbers.keys():
#    if find_student(name):
#        del studens_numbers[name]
#    else:
#        print(f'{name} такого имени нет')
#
#
#def edit (name, new_name):
#   #if name in studens_numbers.keys():
#    if find_student(name):
#        studens_numbers[new_name] = studens_numbers.pop(name)
#
#
#def average_index ():
#    count = len(studens_numbers)
#    rate = sum(studens_numbers.values())
#    return rate / count
#
#
#while True :
#    print(studens_numbers)
#    command = input(f'1) add\n'
#                    f'2) edit\n'
#                    f'3) delete\n'
#                    f'4) average index\n')
#
#    if command == '1':
#        add(name=input('новое имя: '), numbers= int(input('оценка: ')))
#    elif command == '2':
#        edit(name=input('старое имя: '), new_name=input('новое имя: '))
#    elif command =='3':
#        delete(name=input('имя для удаления: '))
#    elif command == '4':
#        print(average_index())
#    else:
#        print('только команда из списка')
#
##edit('vlad', 'vladimir')
##delete('argen')
##add('tima',2)
#print(studens_numbers)




#6.1
#def first_word (word='Hello World'):
#
#    if not isinstance(word, str): #Проверка на строку
#        return False
#
#    First_word = word.split() #Разделяеть предложениена слова
#
#    if First_word:
#        return First_word[0]
#
#    else:
#        return False
#
#print(first_word())
#print(first_word(input('Введите предложение: ')))
#
#6.2
#def process (*numbers):
#    num = len(numbers)
#    suma = 0
#    for _ in numbers:
#        suma += 1
#    answer = sum(numbers) / suma
#    return int(answer)
#
#def average (*args):
#    return int(sum(args) / len(args))
#
#print(process(13,23,43,5653,46,4,5,67,4,3))
#print(average(13,23,43,5653,46,4,5,67,4,3))
#
#6.3
#def verify (password):
#    """Пароль должен содержать не менее 6 символов (букв и цифр!)"""
#
#    if len(password) < 6 :
#        print(verify.__doc__)
#        return False
#    есть_цифры = False
#    есть_буквы = False
#    for i in password :
#       if i.isdigit():  # Если символ - цифра
#           есть_цифры = True
#       elif i.isalpha():  # Если символ - буква
#           есть_буквы = True
#
#    return есть_цифры and есть_буквы
#

#2 вариант
#   if len(password) >= and not password.есть_цифры() and not password.есть_буквы():
#       return True
#   else:
#       return False
#
#print(verify(input("Введите пароль: ")))
#
#7
#
#ten = list(range(1, 11))
#
#evens = tuple(filter(lambda x : x % 2 ==0, ten))
#evens2 = list(map(lambda i : i **2 , evens))
#
#print(evens2)
#
#
#while 1:
#
#    index = input('Введите индекс: ')
#
#    if index.lower() in ['exit', 'выход']:
#       break
#
#    try:
#        index_use = int(index)
#        print(ten[index_use])
#        continue
#
#    except IndexError:
#        print('Индекс только от 0 до 9')
#        continue
#
#    except ValueError:
#        print('Только цифры\nЕсли вы хотите выйти, введите [exit] или [выход]')
#        continue
#
#    except:
#        print('Oops, error')
#        continue
#
# 8
#
#import random
#
#def угадай_число():
#    target_number = random.randint(1, 100)
#    attempts = []
#
#    while True:
#        attempt = int(input('Угадайте число: '))
#        attempts.append(attempt)
#
#        if attempt == target_number:
#            print('Вы угадали число!')
#            сохранить_результат(attempts, target_number)
#            break
#        elif attempt < target_number:
#            print('Больше')
#        else:
#            print('Меньше')
#
#def сохранить_результат(attempts, target_number):
#    att_count = len(attempts)
#    результаты = {
#        'количество_попыток': att_count,
#        'список_попыток': attempts,
#        'загаданное_число': target_number
#    }
#
#    with open('results.txt', 'w', encoding='utf-8') as file:
#        for key, value in результаты.items():
#            file.write(f'{key}: {value}\n')
#
### Запуск игры
#угадай_число()
#
#
#def угадай_число():
#  мин_ч = 1
#  макс_ч = 100
#  at = 0
#
#  while True:
#      at += 1
#      num = (мин_ч + макс_ч) // 2
#      print(f'Ваше число: {num}')
#
#      ответ = input('Введите "больше", "меньше" или "да": ')
#
#      if ответ.lower() == 'больше':
#          мин_ч = num + 1
#      elif ответ.lower() == 'меньше':
#          макс_ч = num - 1
#      elif ответ.lower() == 'да':
#          результат(at, num)
#          break
#      else:
#          print('Неверный ввод. Попробуйте снова.')
#
#def результат(поп, num):
#  результаты = {
#      'количество попыток': at,
#      'Ваше число': num
#  }
#
#  with open('results.txt', 'w', encoding='utf-8') as file:
#      for key, value in результаты.items():
#          file.write(f'{key} - {value}\n')
#
#  print('Результаты сохранены в файле "results.txt".')
#
#
#угадай_число()
#

#OOP


##H/w
#
#class Car:
#    def __init__(self, title, model, weight, hp, nm, max_speed, color):
#        self.title = title
#        self.model = model
#        self.weight = weight
#        self.hp = hp
#        self.nm = nm
#        self.max_speed = max_speed
#        self.color = color
#
#
#    def start_engine(self):
#        print(f"{self.title} {self.model} engine started!")
#
#    def stop_engine(self):
#        print(f"{self.title} {self.model} engine stopped!")
#
#    def info(self):
#        print(f"Title: {self.title}")
#        print(f"Model: {self.model}")
#        print(f"Weight: {self.weight} kg")
#        print(f"Horsepower: {self.hp} hp")
#        print(f"Torque: {self.nm} Nm")
#        print(f"Max Speed: {self.max_speed} km/h")
#        print(f"Color: {self.color}")
#
#
## Создание объектов класса Car
#bmw = Car("BMW", "X5", 2000, 250, 350, 250, "Blue")
#mercedes = Car("Mercedes", "C-Class", 1800, 200, 280, 220, "Silver")
#
## Использование методов
#bmw.start_engine()
#mercedes.start_engine()
#bmw.info()
#mercedes.info()
#bmw.stop_engine()
#mercedes.stop_engine()
#
#
#
#class Company :
#
#    def __init__(self, company_bank, company_name):
#        self.company_bank = company_bank
#        self.company_name = company_name
#
#class Person(Company):
#
#    def __init__(self, company_bank, company_name, first_name, last_name, salary):
#        super().__init__(company_bank, company_name)
#        self.first_name = first_name
#        self.last_name = last_name
#        self.salary = salary
#
#    def get_salary(self):
#        if self.company_bank < self.salary :
#            print(f'У компании недостаточно средств!')
#
#        else:
#            self.company_bank -= self.salary
#            print(f'Зарплата {self.first_name} {self.last_name} выплачено!')
#
#    def person_info(self):
#        print(f'Имя: {self.first_name}')
#        print(f'Фамилия: {self.last_name}')
#        print(f'Зарплата: {self.salary}')
#
#my_company = Company(90000, 'Моя компания')
#
#employee1 = Person(my_company.company_bank, my_company.company_name, "Саша", "Петров", 60000)
#employee2 = Person(my_company.company_bank, my_company.company_name, "Наташа", "Иванова", 40000)
#
#employee1.get_salary()
#employee2.get_salary()
#print()
#employee1.person_info()
#print()
#employee2.person_info()
#
#
#
#class Fraction:
#    def __init__(self, numerator, denominator):
#        self.numerator = numerator
#        self.denominator = denominator
#
#    def __add__(self, other):
#        common_denominator = self.denominator * other.denominator
#        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
#        return Fraction(new_numerator, common_denominator)
#
#    def __sub__(self, other):
#        common_denominator = self.denominator * other.denominator
#        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
#        return Fraction(new_numerator, common_denominator)
#
#    def __mul__(self, other):
#        new_numerator = self.numerator * other.numerator
#        new_denominator = self.denominator * other.denominator
#        return Fraction(new_numerator, new_denominator)
#
#    def __floordiv__(self, other):
#        new_numerator = self.numerator * other.denominator
#        new_denominator = self.denominator * other.numerator
#        return Fraction(new_numerator, new_denominator)
#
#    def simplify(self):
#        # Дополнительный метод для упрощения дроби (если необходимо)
#        com = self.gcd(self.numerator, self.denominator)
#        self.numerator //= com
#        self.denominator //= com
#
#    @staticmethod
#    def gcd(a, b):
#        # Дополнительный статический метод для нахождения наибольшего общего делителя
#        while b:
#            a, b = b, a % b
#        return a
#
## Пример использования
#fraction1 = Fraction(3, 4)
#fraction2 = Fraction(1, 2)
#
#
## Сложение
#result_add = fraction1 + fraction2
#result_add.simplify()
#print(result_add.numerator, '/', result_add.denominator)  # Выведет: 5 / 4
#
## Вычитание
#result_sub = fraction1 - fraction2
#print(result_sub.numerator, '/', result_sub.denominator)  # Выведет: 1 / 4
#
## Умножение
#result_mul = fraction1 * fraction2
#print(result_mul.numerator, '/', result_mul.denominator)  # Выведет: 3 / 8
#
## Целочисленное деление
#result_floordiv = fraction1 // fraction2
#print(result_floordiv.numerator, '/', result_floordiv.denominator)  # Выведет: 3 / 2
#
#
#
#class A:
#
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b
#
#    def __add__(self, other):
#        c = (self.a * other.b ) + (self.b * other.a)
#        d = (self.b * other.b )
#        return A(c, d)
#
#    def __sub__(self, other):
#        c = (self.a * other.b ) - (self.b * other.a)
#        d = (self.b * other.b )
#        return A(c, d)
#
#    def __mul__ (self, other):
#        c = self.a * other.a
#        d = self.b * other.b
#        return A(c, d)
#
#
#
#    def simplify(self):
#    # Дополнительный метод для упрощения дроби (если необходимо)
#        f = self.gcd(self.a, self.b)
#        self.a //= f
#        self.b //= f
#
#    @staticmethod
#    def gcd(a, b):
#        # Дополнительный статический метод для нахождения наибольшего общего делителя
#        while b:
#            a, b = b, a % b
#        return a
#
#
#
#a1 = A(3, 4)
#a2 = A(1, 2)
#result = a1 * a2
##result.simplify()
#print(result.a, '/', result.b)
#

# Работа с файлами
# w - write
# a - add
# x - не создаст новый файл если он уже сущ.
# r - read

# file = open('new_file.txt', 'w', encoding='utf-8') # Только с  русским
# file.write('Бишкек, Кыргызстан')
# file.close()
#
#
# with open('new_file.txt', 'a', encoding='utf-8') as file:
    # file.write('Вторая строка')
#
# with open('n_file.txt', 'x') as file:
    # file.write('4444')
#
#
# with open('new_file.txt', 'w', encoding='utf-8') as file:
    # file.write('Гимн Кыргызстана')
#
#from time import sleep
#
#with open('new_file.txt', 'r', encoding='utf-8') as file:
##    print(file.read())
##    print(file.readlines()[0])
#    for i in file.readlines():
#        sleep()
#        print(i, end='')
#
#print(type(file))

#class Car:
#
#    def __init__(self, model, engine):
#       self.model = model
#       self.engine = engine
#
#    def star_engine(self):
#        print(f'Engine on {self.model} starded')
#
#    def stop_engine(self):
#        print(f'Engine on {self.model} stoped')
#
#
#""" instance Car """
#supra = Car('MK4', '2jz')
#supra.star_engine()
#
#bmw = Car('E38', 'v10' )
#bmw.star_engine()
#

#print(supra.model, supra.engine, supra.hp, supra.nm )

#⁡⁣⁢⁣1 Создайте класс "Student" (Студент), который будет иметь следующие атрибуты:⁡
# ⁡⁣⁢⁣имя (name), возраст (age) и средний балл (gpa).⁡
#
#⁡⁣⁢⁣2 Добавьте метод "init", который будет выполняться при создании нового объекта клас
# ⁡⁣⁢⁣Внутри этого метода установите значения атрибутов "name", "age" и "gpa" на основе
#
#⁡⁣⁢⁣3 Создайте метод "study" (учиться), который будет выводить сообщение о том, что сту
# ⁡⁣⁢⁣заданным именем учится и его средний балл.⁡
#
#⁡⁣⁢⁣4 Создайте метод "graduate" (закончить обучение), который будет выводить сообщение
#⁡⁣⁢⁣ что студент с заданным именем окончил обучение.⁡
#
#⁡⁣⁢⁣5 Создайте два объекта (экземпляра класса) "Student" с разными именами, возрастоми
#
#⁡⁣⁢⁣6 Вызовите метод "study" для каждого объекта, чтобы увидеть сообщение о том,⁡
# ⁡⁣⁢⁣что студент учится и его средний балл.⁡
#
#⁡⁣⁢⁣7 Вызовите метод "graduate" для каждого объекта, чтобы увидеть сообщение о том,⁡
# ⁡⁣⁢⁣что студент окончил обучение.⁡
#
#class student:
#    def __init__(self, name, age, gpa):
#        self.name = name
#        self.age = age
#        self.gpa = gpa
#
#    def study (self):
#        print(f'Cтудент: {self.name}, Возраст: {self.age}, Gpa: {self.gpa} ')
#
#    def graduate (self):
#        print(f'Студент: {self.name} окончил обучение')
#
#
#goodboy = student('G.Kevin', 18, 4.8)
#goodboy.study()
#
#badboy = student('F.Brayn', 19, 3.7)
#badboy.graduate()
#
#
#⁡⁣⁢⁣1 Создайте класс "Person" (Человек), который будет иметь следующие атрибуты: ⁡
#⁡⁣⁢⁣ имя (name), возраст (age) и профессию (profession).⁡
#
#⁡⁣⁢⁣2 Добавьте метод "init", который будет выполняться при создании нового объекта клас
# ⁡⁣⁢⁣Внутри этого метода установите значения атрибутов "name", "age" и "profession" на
#
#⁡⁣⁢⁣3 Создайте метод "introduce" (представиться), который будет выводить сообщение с ⁡
#⁡⁣⁢⁣ информацией о человеке: "Меня зовут [имя]. Мне [возраст] лет и я работаю [професси
#
#⁡⁣⁢⁣4 Создайте два объекта (экземпляра класса) "Person" с разными именами, возрастами и
#
#⁡⁣⁢⁣5 Вызовите метод "introduce" для каждого объекта, чтобы увидеть сообщение с информа
#⁡⁣⁢⁣ ⁡⁣⁢⁣о каждом человеке.⁡
#
#class person:
#    def __init__(self, name, age, profession):
#        self.name = name
#        self.age = age
#        self.profession = profession
#
#    def introduce (self):
#        print(f'Меня зовут {self.name}. Мне {self.age} лет, моя профессия {self.profess
#
#A = person('Сергей', 38, 'Сантехник')
#A.introduce()
#
#B = person('Олег', 25, 'Программист')
#B.introduce()
#
#C = person('Анна', 27, 'Учитель')
#C.introduce()
#
#d_name = input('Имя: ')
#d_age = input('Возраст: ')
#d_profession = input('Профессия: ')
#
#D = person(d_name, d_age, d_profession)
#D.introduce()
#

#⁡⁣⁢⁣1 Создайте класс "BankAccount" (Банковский счет), который будет иметь следующие атр
#⁡⁣⁢⁣ и текущий баланс (balance).⁡
#
#⁡⁣⁢⁣2 Добавьте метод "init", который будет выполняться при создании нового объекта клас
# ⁡⁣⁢⁣Внутри этого метода установите значения атрибутов "owner" и "balance" на основе пе
#
#⁡⁣⁢⁣3 Создайте метод "deposit" (внести депозит), который будет принимать сумму и увелич
#
#⁡⁣⁢⁣4 Создайте метод "withdraw" (снять деньги), который будет принимать сумму и уменьша
#⁡⁣⁢⁣ Убедитесь, что баланс не может стать отрицательным.⁡
#
#⁡⁣⁢⁣5 Создайте объект (экземпляр класса) "BankAccount" с заданным именем владельца счет
#
#⁡⁣⁢⁣6 Вызовите метод "deposit" для объекта "BankAccount" и внесите на счет определенную
#
#⁡⁣⁢⁣7 Вызовите метод "withdraw" для объекта "BankAccount" и снимите сумму со счета. Убе
# ⁡⁣⁢⁣что сумма не превышает текущий баланс.⁡
#
#⁡⁣⁢⁣8 Выведите текущий баланс объекта "BankAccount".
#
#class bankaccount:
#    def __init__(self, owner, balance):
#        self.owner = owner
#        self.balance = balance
#
#    def deposit (self):
#        a = int(input('Внести депозит: '))
#        print(f'Ваш депозит: {a * 5}\nВаш баланс: {self.balance - a }')
#
#    def withdraw (self):
#        b = int(input('Снят денги: '))
#        print(f'Ваш баланс: {self.balance - b}')
#
#
#owner1 = bankaccount('Taylor', 250000)
#owner1.deposit()
#owner1.withdraw()
#
#class BankAccount:
#    def __init__(self, owner, balance):
#        self.owner = owner
#        self.balance = balance
#
#    def deposit(self):
#        amount = float(input('Введите сумму для внесения депозита: '))
#        self.balance += amount
#        print(f'Депозит в размере {amount} успешно внесен. Ваш текущий баланс: {self.ba
#
#    def withdraw(self):
#        amount = float(input('Введите сумму для снятия: '))
#        if amount <= self.balance:
#            self.balance -= amount
#            print(f'Вы успешно сняли {amount}. Ваш текущий баланс: {self.balance}')
#        else:
#            print('Недостаточно средств на счете.')
#
#a = str(input('name: '))
#b = int(input('balance: '))
#owner1 = BankAccount(a, b )
#owner1 = BankAccount('Taylor', 250000)
#owner1.deposit()
#owner1.withdraw()
#
#class Transport:
#    def __init__(self,
#                 title, model, engine,max_speed, speed
#                 ):
#        self.title = title
#        self.model = model
#        self.engine = engine
#        self.max_speed = max_speed
#        self.speed = speed
#
#    def start_engine(self):
#        print(f'Engine on {self.title} {self.model} started!')
#
#
#class Car(Transport):
#
#    current_speed = 0
#
#    def __init__(self, title, model, engine, max_speed, speed, color):
#        super().__init__(title, model, engine, max_speed, speed)
#        self.color = color
#
#    def stop_engine(self):
#        print(f'its stop engine in Car')
#
#    def gas (self):
#        if self.current_speed + self.speed >= self.max_speed:
#            print('CHECK on!')
#        else:
#            self.current_speed += self.speed
#            print(self.current_speed)
#
#    def stop(self):
#        if self.current_speed - self.speed > 0 :
#            self.current_speed -= self.speed
#        else:
#            self.current_speed = 0
#        print(self.current_speed)
#
#
#class Airplane(Transport):
#    def stop_engine(self):
#        print(f'its stop engine in Airplane')
#
#
#bmw = Car('BMW', 'e36', 'v10', 330, 60, 'black')
#
##bmw.start_engine()
##bmw.stop_engine
#
#bmw.gas()
#bmw.gas()
#bmw.gas()
#bmw.gas()
#bmw.gas()
#bmw.gas()
#
#bmw.stop()
#bmw.stop()
#
#boeing = Airplane('Boeing', '77', 'v100', 3600, 600)
#
#boeing.start_engine()
#boeing.stop_engine()

#
#
#class Transport:
#
#    def __init__(self, title, engine, color, model, tachometer):
#        self.title = title
#        self.engine = engine
#        self.color = color
#        self.model = model
#        self.tachometer = tachometer
#
#    def star_engine (self):
#        print(f'On {self.title} {self.model} engine started!')
#
#    def stop_engine(self):
#        print(f'On {self.title} {self.model} engine stop!')
#
#    def car_check (self):
#        if self.tachometer < 1 :
#            print("Check On!")
#
#        else:
#            print('Check off!')
#
#
#class Car(Transport):
#
#    def __init__(self, title, engine, color, model, tachometer, max_speed):
#        super().__init__(title, engine, color, model, tachometer)
#        self.max_speed = max_speed
#
#
#class Tesla(Car):
#    pass
#
#tesla = Tesla(
#    'Tesla',
#    'electra car',
#    'black',
#    'plaid',
#    1,
#    260
#)
#
#print(tesla.max_speed)

#
#tesla = Car(
#    'Tesla',
#    'electra car',
#    'black',
#    'plaid',
#    1,
#    250
#)
#
#tesla.star_engine()
#tesla.car_check()
#
#
#class Animals:
#
#    def __init__(self, name, voice_text):
#        self.name = name
#        self.voice_text = voice_text
#
#    def voice(self):
#        print(f'{self.name} {self.voice_text}')
#
#
#class Dog(Animals):
#    pass
#
#
#class Cat(Animals):
#
#    def voice(self):
#        print(f'I am cat and {self.voice_text}')
#
#    def go_toilet(self):
#        print('I am going pipi')
#
#
#
#sharik = Dog('Sharik', 'GAF GAF')
#murka = Cat('Murka', 'MEOW MEOW')
#
#sharik.voice()
#murka.voice()
#
#
#
#class Human:
#
#    def happy(self):
#        print("Oh I am happy")
#

#lass Animals2:
#
#   def happy(self):
#       print("I am happy animal!")

#
#class Car:
#
#    def __init__(self, title, model, max_speed, speed):
#        self.title = title
#        self.model = model
#        self.max_speed = max_speed
#        self.speed = speed
#        self._current_speed = 0
#
#    def _get_current_speed(self):
#        print(f'Current speed = {self._current_speed}')
#
#
#    def start_engine(self):
#        print(f'{self.title} {self.model} engine started!')
#
#    def gas(self):
#        if self._current_speed + self.speed < self.max_speed:
#            self._current_speed += self.speed
#            self._get_current_speed()
#        else:
#            print("CHECK ON!")
#
#    def stop (self):
#        if self._current_speed - self.speed > 0 :
#            self._current_speed -= self.speed
#            self._get_current_speed()
#        else:
#            print("CHECK ON!")
#
#
#bmw = Car('BMW', "b7", 350, 20)
#bmw.start_engine()
#bmw.gas()
#bmw.gas()
#bmw.gas()
#bmw.gas()
#bmw.gas()
#bmw.gas()
#bmw.gas()
#bmw.gas()
#
#bmw.stop()
#
#
#class A:
#    def __init__(self, num):
#        self.num = num
#
#    def __add__ (self, other):
#        print("Dunder method __add__")
#        self.num += other
#        return self.num
#
#    def __mul__ (self, other):
#        print("Dunder method __mul__")
#        self.num *= other
#        return self.num
#
#    def __sub__ (self, other):
#        print("Dunder method __sub__")
#        self.num -= other
#        return self.num
#
#    def __floordiv__(self, other ):
#        print("Dunder method __floordiv__")
#        self.num //= other
#        return self.num
#
#    def __truediv__(self, other):
#        print("Dunder method __truediv__")
#        self.num /= other
#        return self.num
#
#a1 = A(20)
#print(a1 / 2)
#
#class A:
#
#    def __init__(self, text):
#        self.text = text
#
#    def get_text (self):
#        print(self.text)
#
#class B:
#
#    def test(self):
#        pass
#
#    #Mix class
#
#class C(A, B):
#    pass
#
#
#c1 = C()
#c1.get_text()
#c1.test()
