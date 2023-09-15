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

a = 1

while a :
    list_error = '!@#$%^&*()_+=-/|\?<>:;`~,.'
    password = input('creat a password: ')
    if len(password) < 8 :
        print('password must be 8 characters long')
    if not password.isalnum():
        print('password must contain letters and numbers')

    num = 0
    let = ''

    for i in password :
        if i in list_error :
            print('password must not contain: "!@#$%^&*()_+=-/|?<>:;`~,."')

        if i.isnumeric():
            num += int(i)
        else:
            let += i

    print(num, let)
#
