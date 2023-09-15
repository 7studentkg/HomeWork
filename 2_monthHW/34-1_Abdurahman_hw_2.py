# print('HomeWork №2 Level: easy*\n')
#
# class Figure:
    # unit = 'cm'
    # def __init__(self):
        # pass
#
    # def calculate_area(self):
        # pass
#
    # def info(self):
        # pass
#
# class Circle(Figure):
    # def __init__(self, radius):
        # super().__init__()
        # self.__radius = radius
        # if self.__radius < 0 :
            # raise ValueError("radius must be more zero")
#
#
    # def calculate_area(self):
#
#
        # return 3.14 * self.__radius**2
#
#
    # def info(self):
        # print(f'Circle radius: {self.__radius}{self.unit},\n'
            #   f'Area: {self.calculate_area()}{self.unit}.\n')
#
#
# class RightTriangle(Figure):
    # def __init__(self, side_a, side_b):
        # super().__init__()
        # self.__side_a = side_a
        # self.__side_b = side_b
        # if self.__side_a < 0 or self.__side_b < 0 :
            # raise ValueError('side or sides must be more zero')
#
    # def calculate_area(self):
        # return self.__side_a* self.__side_b / 2
#
    # def info(self):
        # print(f'RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit},\n'
            #   f'Area: {self.calculate_area()}{self.unit}.\n')
#
#
# circle1 = Circle(2)
# circle2 = Circle(7)
# triangle1 = RightTriangle(5, 8)
# triangle2 = RightTriangle(3, 7)
# triangle3 = RightTriangle(9, 12)
#
# figures_list = [circle1, circle2, triangle1, triangle2, triangle3]
#
# for figure in figures_list:
    # figure.info()
#

print('HomeWork №2 Level: hard**\n')

# 2.0
class Figure:
    unit = 'cm'
    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter (self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
        self.perimeter = self.calculate_perimeter()
        if self.__side_length < 0 :
            raise ValueError('side lenght must be more zero')

    def calculate_area(self):
        return self.__side_length ** 2

    def calculate_perimeter(self):
        return self.__side_length * 4

    def info (self):
        self.calculate_perimeter()
        print(f'Square side length: {self.__side_length}{self.unit}, Perimeter: {self.perimeter}{self.unit}, '
              f'Area: {self.calculate_area()}{self.unit}.\n')


class Rectangle(Figure):
    def __init__(self, lenght, width):
        super().__init__()
        self.__lenght = lenght
        self.__width = width
        self.perimeter = self.calculate_perimeter()
        if self.__lenght < 0 :
            raise ValueError('lenght must be more zero')
        if self.__width < 0 :
            raise ValueError('width must be more zero')


    def calculate_area(self):
        return self.__width * self.__lenght

    def calculate_perimeter(self):
        return ( self.__lenght + self.__width ) * 2

    def info (self):
        self.calculate_perimeter()
        print(f'Rectangle length: {self.__lenght}{self.unit}, width: {self.__width}{self.unit}, '
              f'Perimeter: {self.perimeter}{self.unit}, Area: {self.calculate_area()}{self.unit}.\n')


square1 = Square(5)
square2 = Square(9)
rectangle1 = Rectangle(5, 8)
rectangle2 = Rectangle(7, 3)
rectangle3 = Rectangle(2, 6)

list_figures = [square1, square2, rectangle1, rectangle2, rectangle3]

for figures in list_figures:
    figures.info()

# 1.0
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
