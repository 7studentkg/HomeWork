print("Home Work №7\n")

ten = list(range(1, 11))
even = list(filter(lambda num : num % 2 == 0 , ten))
square_even = list(map(lambda num: num**2 , even))

print(ten, even, square_even, sep='\n')

def index (list_index=ten):
    while 1 :
        try:
            index_enter = input('Enter index: ')
            index2 = f'от 0 до {len(list_index)-1}'
            if index_enter.lower() == 'exit' or index_enter.lower() == 'выход':
                break
            index_enter = int(index_enter)
            print(list_index[index_enter])

        except IndexError:
            print(f'Неправильный индекс ! \nИндекст {index2}')
        except ValueError:
            print('Error! >> Только целые числа ')
            #print('Oops Error!\nТолько индексы из аргумнета << {} >>'.format(list_index))


index()
#index('Python')
#index('Kyrgyzstan')
#index(range(19))
