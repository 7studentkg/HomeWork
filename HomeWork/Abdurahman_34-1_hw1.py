print("Home Work №1\nНаписать программу для вычисления расходов за неделю.\n")

Monday = int(input('Monday: '))
Tuesday = int(input('Tuesday: '))
Wednesday = int(input('Wednesday: '))
Thursday = int(input('Thursday: '))
Friday = int(input('Friday: '))
Saturday = int(input('Saturday: '))
Sunday = int(input('Sunday: '))

sum_days = Monday + Tuesday + Wednesday +\
            Thursday + Friday + Saturday + Sunday

print(f'Общая сумма расходы за неделю {sum_days} сомов,\
        ну или долларов как хотите :)')

amount_weekend = 7
average_day = sum_days / amount_weekend

print(f'Средний расход за день {round(average_day, 1)}')


s = 0
i = 0
while i < 7:
    i += 1
    p = float(input("Введите расходы за день: "))
    s += p
    print(s)

print(f'средный расход за день  {round(s / 7, 1)}')
