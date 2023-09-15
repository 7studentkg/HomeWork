class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, other):
        self.__cpu = other

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, other):
        self.__memory = other

    def make_computations(self):
        add_result = self.__cpu + self.__memory
        sub_result = self.__cpu - self.__memory
        mult_result = self.__cpu * self.__memory
        if self.__memory == 0 :
            raise ZeroDivisionError('Делит на ноль нельзя! ты что, в школе не учился ?')
        else:
            div_result = round(self.__cpu / self.__memory, 2)

        return f'Add: {add_result}\nSub: {sub_result}\nMult: {mult_result}\nDiv: {div_result}'


    def __str__(self):
        return (f'CPU: {self.__cpu} MEMORY: {self.__memory}')

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list


    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    @sim_cards_list.setter
    def sim_cards_list(self, other):
        self.__sim_cards_list = other

    def call (self, sim_cards_number, call_to_number):
        return (f'“Идет звонок на номер {sim_cards_number}” с сим-карты - {call_to_number}')

    def __str__(self):
        return (f'SIM CARDS: {self.__sim_cards_list}')


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)


    def __str__(self):
        return (f"SmartPhone -  CPU: {self.cpu} MEMORY: {self.memory} SIM CARDS: {self.sim_cards_list}")

    def use_gps(self, location):
        return (f'GPS включен. Прокладываем маршрут до {location}...')


computer = Computer(86, 300)
print(f'Computer - {computer}')

phone = Phone(['Megacom', 'O!', 'Beeline'])
print(f'Phone - {phone}')

Iphone1 = SmartPhone(13, 128, 'Megacom')
Iphone2 = SmartPhone(14, 256, 'O!')
print(Iphone1)
print(Iphone2)

print(f'CPU: {computer.cpu}')
computer.cpu = 32
print(f'NEW CPU: {computer.cpu}')

print(f'MEMORY: {computer.memory}')
computer.memory = 250
print(f'NEW MEMORY: {computer.memory}')

print(computer.make_computations())

print('computer < new computer: ', computer < Computer(64, 450))
print('computer > new computer: ', computer > Computer(64, 450))
print('computer == new computer: ', computer == Computer(64, 450))
print('computer != new computer: ', computer != Computer(64, 450))
print('computer <= new computer: ', computer <= Computer(64, 450))
print('computer >= new computer: ', computer >= Computer(64, 450))

print(Iphone1.call('+996 312 312 312', f'{Iphone1.sim_cards_list}'))
print(Iphone2.use_gps('Балыкчы'))
