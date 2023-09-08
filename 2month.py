class Transport:

    def __init__ (self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color
        print(f'{self.model} changed color')

class Plane(Transport):
    def __init__ (self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    counter = 0
    weels_standart_number = 4


    def __init__ (self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)
        Car.counter += 1

    def drive(self, city):
        print(f'Car {self.model} is driving {city}')


print(f'Car factory produce: {Car.counter}')

bmw_car = Car('BMW X5', 2020, 'Black')
print(f'MODEL: {bmw_car.model}, YEAR: {bmw_car.year}, COLOR: {bmw_car.color}')

#bmw_car.color = 'Red'
bmw_car.change_color('Red')
print(f'MODEL: {bmw_car.model}, YEAR: {bmw_car.year}, NEW COLOR: {bmw_car.color}')

honda_car = Car(the_year= 2019, the_color='Silver', the_model='Honda CR-V')
print(f'MODEL: {honda_car.model}, YEAR: {honda_car.year}, COLOR: {honda_car.color}')

honda_car.drive('Osh')

print(f'Car factory produce: {Car.counter}')

price_for_wheels_lastic = 5000
print(f'We need {Car.counter * Car.weels_standart_number * price_for_wheels_lastic} soms to change our car ')
