# ⁡⁣⁣⁡⁢⁢⁣⁡⁣⁢⁡⁢⁣⁣​‌‍‌⁡⁢⁢⁢⁡⁣⁢⁣⁡⁢⁣⁢𝗧𝗲𝘀𝘁 ⁡⁡⁡​⁡⁡⁡⁡


#
#resorts = ['Сочи', 'курорты Краснодарского Края', 'Санкт-Петербург', 'Карелию']
#def choose_vacation_place(resorts):
#    for resort in resorts:
#        if resort == 'Сочи':
#            return resort
#resort = choose_vacation_place(resorts)
#print('Поехали в ' + resort)
#

#
#import random
#
#lower = "abcdefghijklmnopqrstuvwxyz"
#upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#numbers = "0123456789"
#symbols = "[}{}()*;/,._-"
#
#all = lower + upper + numbers + symbols
#lenght = 16
#password = "".join(random.sample(all,lenght))
#
#print(password)
#
#Объявите функцию rooms_equal() с параметрами room_size и room_list
#def rooms_equal(room_size, room_list):
# Перенесите следующий код в тело функции, которую вы объявили
#   count = 0
#
#   for room in room_list:
#       if room == room_size:
#           count = count + 1
#
#   print('Комнат площадью', room_size, 'кв.м:', count)
#
#
# Следующий код не изменяйте и не переносите в тело функции
#flat = [
#   5.55, 22.19, 7.78, 26.86, 5.55,
#   29.84, 22.19, 5.55, 16.85, 4.52
#
#
#hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]
#
#rooms_equal(5.55, flat)
# Добавьте ещё один вызов функции rooms_equal()
# Передайте в функцию искомую площадь - 9.2 кв.м и список hut
#rooms_equal(9.2, hut)
#
#def number_of_occurrences(char, string):
#    # Здесь объявите переменную count, равную нулю.
#    # Она будет хранить количество вхождений
#    count = 0
#    for letter in string:
#        # Напишите условие: сравните переменные letter и char
#        # И если letter равна char - увеличивайте счётчик count на 1
#        if letter == char:
#            count += 1
#
#    # Печатаем исходную строку:
#    print('Исходная строка:', string)
#    # Печатаем результат подсчётов:
#    print('Количество вхождений символа', char, 'составляет:', count)
#
#
## Код ниже не изменяйте
#phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'
#
## Вызываем функцию number_of_occurrences(), чтобы она посчитала,
## сколько раз во фразе phrase встречается буква 'е'
#number_of_occurrences('е', phrase)
#
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
#d = "I" "love" "arrays they are my favorite"
#a = d.find('love')
#print(a)
#
#
#
#hello = {
#    'english': 'Welcome',
#    'czech': 'Vitejte',
#    'danish': 'Velkomst',
#    'dutch': 'Welkom',
#    'estonian': 'Tere tulemast',
#    'finnish': 'Tervetuloa',
#    'flemish': 'Welgekomen',
#    'french': 'Bienvenue',
#    'german': 'Willkommen',
#    'irish': 'Failte',
#    'italian': 'Benvenuto',
#    'latvian': 'Gaidits',
#    'lithuanian': 'Laukiamas',
#    'polish': 'Witamy',
#    'spanish': 'Bienvenido',
#    'swedish': 'Valkommen',
#    'welsh': 'Croeso'
#}
#
#def greet(language):
#    for language in hello:
#        if language == hello():
#            return language.values()
#        else:
#            return 'Welcome'
#
#greet('german')
#
#⁡⁢⁣⁢"""⁡
#   ⁡⁢⁣⁢ ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⁡
#    ⁡⁢⁣⁢⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⁡
# ⁡⁢⁣⁢   ⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⁡
#   ⁡⁢⁣⁢ ⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⁡
#  ⁡⁢⁣⁢  ⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿⁡
#  ⁡⁢⁣⁢  ⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿⁡
# ⁡⁢⁣⁢   ⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿⁡
# ⁡⁢⁣⁢   ⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿⁡
#  ⁡⁢⁣⁢  ⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼⁡
#   ⁡⁢⁣⁢ ⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼⁡
#    ⁡⁢⁣⁢⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿⁡
#   ⁡⁢⁣⁢ ⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿⁡
#    ⁡⁢⁣⁢⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿⁡
#    ⁡⁢⁣⁢⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿⁡
#    ⁡⁢⁣⁢⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⁡
#    ⁡⁢⁣⁢⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⁡
#    ⁡⁢⁣⁢⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⁡
#    ⁡⁢⁣⁢⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⁡
#  ⁡⁢⁣⁢  ⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⁡
#⁡⁢⁣⁢    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⁡
#  ⁡⁢⁣⁢  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⁡
#   ⁡⁢⁣⁢ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⁡
#    ⁡⁢⁣⁢⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⁡
#    ⁡⁢⁣⁢⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉⁡
#    ⁡⁢⁣⁢⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤⠄⁡
#
#    ⁡⁢⁣⁢"""⁡
#



print(-2+4)



#
#a = '4 5'.split(' ')
#
#print(int(a[0]) + int(a[1]))

#
#def first_word(text: str) -> str:
#    # your code here
#    return text.split()[0]   #выводить первое слово
#
#
##print("Example:")
#print(first_word("Hello world"))

#def first_word(text: str) -> str:
#    # your code here
#    return text.split(' ')
##
##
##print("Example:")
#print(first_word("HelloWorld"))
#
#
#import re
#def solution(s):
#    return re.sub('([A-Z])', r' \1', s)
#
#
#numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3]
#
#a = {num for num in numbers}
#
#print(a)
#
#
#a = print

#a( "Hello")


#quote_1 = 'Работает? Не трогай'
#quote_2 = 'Если твой код работает, значит это хороший код'
#quote_3 = 'Лень - главное достоинство программиста'
#
#def penult_word(message):
#    word_list = message.split()
#
#    return word_list[-3]
#
## Вызовы функции готовы к работе, не изменяйте их!
## Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
#
#print(penult_word(quote_1))
#
## То же, но с аргументом quote_2.
#print(penult_word(quote_2))
##
## То же с аргументом quote_3.
#print(penult_word(quote_3))
#

#def check_query(query):
#
#    e = query.split(',')
#
#    if "Анфиса" in e:
#        return 'запрос к Анфисе'
#    else:
#        return 'запрос к кому-то ещё'
#
#
#queries = [
#    'Анфиса, сколько у меня друзей?',
#    'Андрей, ну где ты был?',
#    'Андрей, ну обними меня скорей!',
#    'Анфиса, кто все мои друзья?'
#]
#
#for q in queries:
#
#    result = check_query(q)
#
#    print(q, '-', result)
#
#
#def check_query(query):
#    elements  = query.split(', ')
#    # Напишите код функции
#    return elements[1]
#
## Дальше следует код, вызывающий вашу функцию; не изменяйте его:
#queries = [
#    'Анфиса, сколько у меня друзей?',
#    'Андрей, ну где ты был?',
#    'Андрей, ну обними меня скорей!',
#    'Анфиса, кто все мои друзья?'
#]
#
#for q in queries:
#    result = check_query(q)
#    print(q, '—', result)
#
#
#words_list = ['раз', 'два', 'три', 'четыре', 'пять', 'вышел', 'зайчик', 'погулять']
## Метод join() "склеивает" элементы списка,
## создавая строку, в которой
## элементы исходного списка разделены текстовым символом;
## для разделения применим дефис:
#new_string = '-'.join(words_list)
#
#print(new_string)
#
#
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
#
#        return 'У тебя ' + str(count) + ' друзей.'
#    elif query == 'Кто все мои друзья?':
#        # Из словаря DATABASE создайте строку с помощью join();
#        # имена друзей разделите запятой и пробелом.
#        # Запишите эту строку в переменную friends_string (вместо пустых кавычек).
#        friends_string = ', '.join(DATABASE)
#
#        # Этот цикл больше не понадобится, удалите его
#      #  for friend in DATABASE:
#       #     friends_string += friend + ' '
#
#        return 'Твои друзья: ' + friends_string
#    elif query == 'Где все мои друзья?':
#        unique_cities = set(DATABASE.values())
#        # Из сета unique_cities создайте строку с помощью join();
#        # названия городов разделите запятой и пробелом.
#        # Запишите эту строку в переменную cities_string (вместо пустых кавычек).
#        cities_string = ', '.join(unique_cities)
#
#        # Этот цикл больше не понадобится, удалите его
#       # for city in unique_cities:
#       #     cities_string += city + ' '
#
#        return 'Твои друзья в городах: ' + cities_string
#    else:
#        return '<неизвестный запрос>'
#
#
#print('Привет, я Анфиса!')
#print(process_anfisa('Сколько у меня друзей?'))
#print(process_anfisa('Кто все мои друзья?'))
#print(process_anfisa('Где все мои друзья?'))
#
#
#
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
#
#def format_friends_count(friends_count):
#    if friends_count == 1:
#        return '1 друг'
#    elif 2 <= friends_count <= 4:
#        return f'{friends_count} друга'
#    else:
#        return f'{friends_count} друзей'
#
#
#def process_anfisa(query):
#    if query == 'сколько у меня друзей?':
#        count = len(DATABASE)
#
#        return f'У тебя {format_friends_count(count)}.'
#    elif query == 'кто все мои друзья?':
#        friends_string = ', '.join(DATABASE)
#        return f'Твои друзья: {friends_string}'
#    elif query == 'где все мои друзья?':
#        unique_cities = set(DATABASE.values())
#        cities_string = ', '.join(unique_cities)
#        return f'Твои друзья в городах: {cities_string}'
#    else:
#        return '<неизвестный запрос>'
#
#def process_friends(name, query):
#    if name in DATABASE:
#        if query == 'ты где?':
#            city = DATABASE[name]
#            return f'{name} в городе {city}'
#        elif  not query =='ты где?':
#            return '<неизвестный запрос>'
#    elif name not in  DATABASE:
#        return f'У тебя нет друга по имени {name}'
#
#    else:
#        return '<неизвестный запрос>'
#
#def process_query(query):
#    q = query.split(', ')
#    if q[0] == 'Анфиса':
#   # if 'Анфиса' in query:
#       # return process_anfisa(' '.join(query[1::]))
#       return process_anfisa(q[1])
#    else:
#       return process_friends(q[0], q[1])
#
#print('Привет, я Анфиса!')
#print(process_query('Анфиса, сколько у меня друзей?'))
#print(process_query('Анфиса, кто все мои друзья?'))
#print(process_query('Анфиса, где все мои друзья?'))
#print(process_query('Анфиса, кто виноват?'))
#print(process_query('Соня, ты где?'))
#print(process_query('Коля, что делать?'))
#print(process_query('Антон, ты где?'))
#
