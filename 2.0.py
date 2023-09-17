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
#⁡⁣⁢⁣2 Добавьте метод "init", который будет выполняться при создании нового объекта класса "Student".⁡
# ⁡⁣⁢⁣Внутри этого метода установите значения атрибутов "name", "age" и "gpa" на основе переданных значений.⁡
#
#⁡⁣⁢⁣3 Создайте метод "study" (учиться), который будет выводить сообщение о том, что студент с⁡
# ⁡⁣⁢⁣заданным именем учится и его средний балл.⁡
#
#⁡⁣⁢⁣4 Создайте метод "graduate" (закончить обучение), который будет выводить сообщение о том,⁡
#⁡⁣⁢⁣ что студент с заданным именем окончил обучение.⁡
#
#⁡⁣⁢⁣5 Создайте два объекта (экземпляра класса) "Student" с разными именами, возрастоми средними баллами.⁡
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
#⁡⁣⁢⁣2 Добавьте метод "init", который будет выполняться при создании нового объекта класса "Person".⁡
# ⁡⁣⁢⁣Внутри этого метода установите значения атрибутов "name", "age" и "profession" на основе переданных значений⁡.
#
#⁡⁣⁢⁣3 Создайте метод "introduce" (представиться), который будет выводить сообщение с ⁡
#⁡⁣⁢⁣ информацией о человеке: "Меня зовут [имя]. Мне [возраст] лет и я работаю [профессия]".⁡
#
#⁡⁣⁢⁣4 Создайте два объекта (экземпляра класса) "Person" с разными именами, возрастами и профессиями.⁡
#
#⁡⁣⁢⁣5 Вызовите метод "introduce" для каждого объекта, чтобы увидеть сообщение с информацией⁡
#⁡⁣⁢⁣ ⁡⁣⁢⁣о каждом человеке.⁡
#
#class person:
#    def __init__(self, name, age, profession):
#        self.name = name
#        self.age = age
#        self.profession = profession
#
#    def introduce (self):
#        print(f'Меня зовут {self.name}. Мне {self.age} лет, моя профессия {self.profession}.')
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

#⁡⁣⁢⁣1 Создайте класс "BankAccount" (Банковский счет), который будет иметь следующие атрибуты: имя владельца счета (owner) ⁡
#⁡⁣⁢⁣ и текущий баланс (balance).⁡
#
#⁡⁣⁢⁣2 Добавьте метод "init", который будет выполняться при создании нового объекта класса "BankAccount". ⁡
# ⁡⁣⁢⁣Внутри этого метода установите значения атрибутов "owner" и "balance" на основе переданных значений.⁡
#
#⁡⁣⁢⁣3 Создайте метод "deposit" (внести депозит), который будет принимать сумму и увеличивать текущий баланс на эту сумму.⁡
#
#⁡⁣⁢⁣4 Создайте метод "withdraw" (снять деньги), который будет принимать сумму и уменьшать текущий баланс на эту сумму.⁡
#⁡⁣⁢⁣ Убедитесь, что баланс не может стать отрицательным.⁡
#
#⁡⁣⁢⁣5 Создайте объект (экземпляр класса) "BankAccount" с заданным именем владельца счета и начальным балансом.⁡
#
#⁡⁣⁢⁣6 Вызовите метод "deposit" для объекта "BankAccount" и внесите на счет определенную сумму.⁡
#
#⁡⁣⁢⁣7 Вызовите метод "withdraw" для объекта "BankAccount" и снимите сумму со счета. Убедитесь,⁡
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
#        print(f'Депозит в размере {amount} успешно внесен. Ваш текущий баланс: {self.balance}')
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
