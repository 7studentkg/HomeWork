#6. Добавить в класс Figure нереализованный публичный метод calculate_perimeter (подсчет периметра фигуры)
#10. В конструкторе класса Square должен высчитываться периметр квадрата, посредством вызова метода calculate_perimeter
#и возвращаемый результат метода задавался бы атрибуту perimeter.
#12. В классе Square переопределить метод calculate_perimeter, который бы считал и возвращал периметр квадрата.
#16. В конструкторе класса Rectangle должен высчитываться периметр прямоугольника, посредством вызова метода calculate_perimeter
# и возвращаемый результат метода задавался бы атрибуту perimeter.
#18. В классе Rectangle переопределить метод calculate_perimeter, который бы считал и возвращал периметр прямоугольника.
#
# class Figure:
    # unit = 'cm'
#
    # def __init__(self):
        # self.__perimeter = 0
#
    # @property
    # def perimeter(self):
        # return self.__perimeter
#
    # @perimeter.setter
    # def perimeter(self, value):
        # self.__perimeter = value
#
    # def calculate_area(self):
        # pass
#
    # def calculate_perimeter(self):
        # pass
#
    # def info(self):
        # pass
#
#
# class Square(Figure):
    # def __init__(self, side_length):
        # super().__init__()
        # self.__side_length = side_length
        # self.calculate_perimeter()
        # if self.__side_length < 0 :
            # raise ValueError('side lenght must be more zero')
#
    # def calculate_area(self):
        # return self.__side_length ** 2
#
    # def calculate_perimeter(self):
        # self.perimeter = self.__side_length * 4
#
    # def info(self):
        # print(f'Square side length: {self.__side_length}{self.unit},\n'
            #   f'Perimeter: {self.perimeter}{self.unit}, Area: {self.calculate_area()}{self.unit}.\n')
#
#
# class Rectangle(Figure):
    # def __init__(self, length, width):
        # super().__init__()
        # self.__length = length
        # self.__width = width
        # self.calculate_perimeter()
        # if self.__length < 0 :
            # raise ValueError('lenght must be more zero')
        # if self.__width < 0 :
            # raise ValueError('width must be more zero')
#
    # def calculate_area(self):
        # return self.__length * self.__width
#
    # def calculate_perimeter(self):
        # self.perimeter = (self.__length + self.__width) * 2
#
    # def info(self):
        # print(f'Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit},\n'
            #   f'Perimeter: {self.perimeter}{self.unit}, Area: {self.calculate_area()}{self.unit}.\n')
#
#
# square1 = Square(5)
# square2 = Square(9)
# rectangle1 = Rectangle(5, 8)
# rectangle2 = Rectangle(7, 3)
# rectangle3 = Rectangle(2, 6)
#
# list_figures = [square1, square2, rectangle1, rectangle2, rectangle3]
#
# for figures in list_figures:
    # figures.info()
#
#
# print('HomeWork №2 Level: hard**\n')
#
# class Figure:
    # unit = 'cm'
    # def __init__(self, perimeter=0):
        # self.__perimeter = perimeter
#
    # @property
    # def perimeter(self):
        # return self.__perimeter
#
    # @perimeter.setter
    # def perimeter (self, value):
        # self.__perimeter = value
#
    # def calculate_area(self):
        # pass
#
    # def calculate_perimeter(self):
        # pass
#
    # def info(self):
        # pass
#
#
# class Square(Figure):
    # def __init__(self, side_length, perimeter=0):
        # super().__init__(perimeter)
        # self.__side_length = side_length
        # if self.__side_length < 0 :
            # raise ValueError('side lenght must be more zero')
#
    # def calculate_area(self):
        # return self.__side_length ** 2
#
    # def calculate_perimeter(self):
        # self.__perimeter = self.__side_length*4
#
    # def info (self):
        # self.calculate_perimeter()
        # print(f'Square side length: {self.__side_length}{self.unit}, Perimeter: {self.__perimeter}{self.unit},\n'
            #   f'Area: {self.calculate_area()}{self.unit}.\n')
#
#
# class Rectangle(Figure):
    # def __init__(self, lenght, width, perimeter=0):
        # super().__init__(perimeter)
        # self.__lenght = lenght
        # self.__width = width
        # if self.__lenght < 0 :
            # raise ValueError('lenght must be more zero')
        # if self.__width < 0 :
            # raise ValueError('width must be more zero')
#
#
    # def calculate_area(self):
        # return self.__width * self.__lenght
#
    # def calculate_perimeter(self):
        # self.__perimeter = ( self.__lenght + self.__width ) * 2
#
    # def info (self):
        # self.calculate_perimeter()
        # print(f'Rectangle length: {self.__lenght}{self.unit}, width: {self.__width}{self.unit},\n'
            #   f'Perimeter: {self.__perimeter}{self.unit}, Area: {self.calculate_area()}{self.unit}.\n')
#
#
# square1 = Square(5)
# square2 = Square(9)
# rectangle1 = Rectangle(5, 8)
# rectangle2 = Rectangle(7, 3)
# rectangle3 = Rectangle(2, 6)
#
# list_figures = [square1, square2, rectangle1, rectangle2, rectangle3 ]
#
# for figures in list_figures:
    # figures.info()
#
#
# all = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm'
# g ='aeiouyауоеёяиюэы'


# while True:

    # gl = 0
    # sogl = 0
    # s = 0

    # word= input("Введите слово: ")


    # for i in word.lower():
        # if i in all:
            # s += 1
            # if  i in g:
                # gl+=1
            # else:
                # sogl+=1
    # if word == 'stop':
        # print("Thanks bruh")
        # break

    # print(f'Слово:{word}')
    # print(f'Количество букв:{s}')
    # print(f'Согласных: {sogl}')
    # print(f'Гласных: {gl}')
    # print(f'Процент Гласных: {round(gl / s * 100, 2)}; Процент Согласных: {round(sogl / s * 100, 2)}')
#
# list_error = '!@#$%^&*()_+=-/|\?<>:;`~,.' # это символы которые не допускаются оно еще не работает
#
# while True:
    # password = input('creat a password: ')
    # if password == 'stop': # специальное слово
        # print("Goodbay")
        # break
    # if len(password) < 8 : # пароль должен содержать 8 символом или более
        # print('password must be 8 characters long')
#
    # num = 0
    # let = ''
#
    # for i in password :# тут мы перебераетм каждую буквы из пароля
        # if i in list_error :
            # print('password must not contain: "!@#$%^&*()_+=-/|?<>:;`~,."')
#
        # if i.isnumeric(): # этот метот отлавливает цифры из пароля вне зависимости что оно типа str
            # num += int(i)
        # elif i.isalpha: # Это буквы
            # let += i
#
    # for i in list_error:
        # if i in let:
            # let.remove(i)
#
#
#
    # print(num)
    # print(let)

#
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
# class Car:
    # def __init__(self, model, year, color):
        # self.__model = model
        # self.__year = year
        # self.__color = color
#
    # @property
    # def model(self):
        # return self.__model
#
    # @property
    # def year(self):
        # return self.__year
#
    # @property
    # def color(self):
        # return self.__color
#
    # @color.setter
    # def color(self, value):
        # self.__color = value
#
    # def drive(self):
        # print(f'car: {self.__model} is driving')
#
    # def __str__(self):
        # return f'MODEL: {self.__model}, YEAR: {self.__year}, COLOR: {self.__color} '
#
#
# class FuelCar(Car):
    # def __init__(self, model, year, color, fuel_bank):
        # Car.__init__(self, model, year, color)
        # self.__fuel_bank = fuel_bank
#
    # @property
    # def fuel_bank(self):
        # return self.__fuel_bank
#
    # def drive(self):
    #    print(f'car: {self.__model} is driving by fuel')
#
    # def __str__(self):
        # return super().__str__() + f' FUEL BANK: {self.__fuel_bank}'
#
# class ElectricCar(Car):
    # def __init__(self, model, year, color, battery):
        # Car.__init__(self, model, year, color)
        # self.__battery = battery
#
    # @property
    # def battery(self):
        # return self.__battery
#
    # def drive(self):
        # print(f'car: {self.__model} is driving by electricity')
#
    # def __str__(self):
        # return super().__str__() + f'Battery BANK: {self.__battery}'
#
#
# class HybridCar(FuelCar, ElectricCar):
    # def __init__(self, model, year, color, fuel_bank, battery):
        # FuelCar.__init__(self, model, year, color, fuel_bank)
        # ElectricCar.__init__(self, model, year, color, battery)
#
#
# some_car = Car('BMW X6', 2023, 'Black')
# print(some_car)
# nissan_car = FuelCar('Nissan Patrol', 2009, 'White', 10)
# print(nissan_car)
#
# toyota_car = HybridCar('Prius',2023,'white', 45, 45000)
# print(toyota_car)
#
