# ⁡⁣⁢​‌‍‌⁣Convert a String to a Number!​

#def string_to_number(s):    #0 '1234' => 1234
#
#    return int(s)           #1 option
#
#    return float(s)         #2 option
#
#    return eval(s)          #3 option
#
#    if s.isdigit():         #4 option
#        return int(s)
#    else:
#        return float(s)

# ​‌‍‌Reversed Strings​

#def solution(string):       #0 'Python' => 'nohtyP'
#
#    return string[::-1]     #1 option
#
#   temp = list(string)      #2 option
#   temp.reverse()
#   return ''.join(temp)
#

# ​‌‍‌Check same case​

#def same_case(a, b):
#
#    if not a.isalpha() or not b.isalpha():     #1 option              #0  #'a' and 'g' returns 1
#        return -1
#                                                                          #'A' and 'C' returns 1
#    if a.isupper() == b.isupper():
#        return 1                                                          #'b' and 'G' returns 0
#
#    else:                                                                 #'B' and 'g' returns 0
#        return 0
#                                                                          #'0' and '?' returns -1

#    if a.isalpha() and b.isalpha():            #2 option
#        if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
#            return 1
#        else:
#            return 0
#    else:
#        return -1
#
# ​‌‍‌Calculate BMI​

#def bmi(weight, height):
#    #your code here
#    if weight / pow(height, 2) <= 18.5:
#        return  "Underweight"
#    elif weight / pow(height, 2) <= 25.0:
#        return "Normal"
#    elif weight / pow(height, 2) <= 30.0:
#        return "Overweight"
#    else:
#        return "Obese"

#def bmi(weight, height):
#    bmi = weight / height ** 2
#    if bmi <= 18.5:
#        return "Underweight"
#    elif bmi <= 25:
#        return "Normal"
#    elif bmi <= 30:
#        return "Overweight"
#    else:
#        return "Obese"

# Hello world
#def greet():
#    poem = []
#
#    poem.append("h is for happy")
#    poem.append("e is for energy")
#    poem.append("l is for love")
#    poem.append("l is also for life")
#    poem.append("o is for original like this poem")
#    poem.append(" ")
#    poem.append("w is for your well-being")
#    poem.append("o is for optimism which we all should have")
#    poem.append("r is for rest which we all need more")
#    poem.append("l is longing for a better future")
#    poem.append("d is a deep-felt thanks for reading this poem")
#    poem.append("! <3<3<3")
#
#    return ''.join(p[0] for p in poem)
#
#def greet():
#    grt = "!dlrow olleh"
#    return grt[::-1]

#
#
#print(len("Hello"))
#
#count = 0
#for i in "Hello":
#    count +=1
#
#print(count)

#
#def lenb(a):
#    count = 0
#    for _ in a:
#        count += 1
#    return count
#
#
#print(lenb('asdf'))
#print(len("fdsa"))
#print(lenb(input('write: ')))
#
#
#def square (width, length):
#    return width * length
#
#a = square(7, 4)
#b = square(8, 14)
#
#print(a, b, sep='\n')
#print(a, b, end='\n')

#
#def square (width: int , length: int) -> int:
#    """Hello guys""" #документация
#    return width * length
#
#print(square(3, 5))
#print(square.__doc__) # """Hello guys"""
#print(help(square))
#

#def two(*args):
#    print(args)
#    return sum(args)
#
#def two (a, b=1, *args):
#    print(a, b, args)
#    return sum(args) / a * b
#
#def two (a, *args, b=4):
#    print(a, b, args)
#    return sum(args) / a * b
#
#print(two(4, 8, 34, 7, 75))
#
#def one (**kwargs):
#    #return kwargs
#    return sum(kwargs.values())
#
#print(one(a=3, b=2, c=1)) #словарь
#
#lambda arguments: expression (Формула)
#map, filter, sorted
#
#lambda_func = lambda a, b: a + b
#print(lambda_func(2, 3))
#
#
#def abC(word='hello'):
#    return word[:-1] + word[-1].title()
#
#print(abC())
#
#
#numbers = list(range(1, 11))
#
#new = list(map(lambda x: x *3, numbers))
#new2 = list(map(str, numbers))
#new3 = [i*2 for i in numbers]
#
#print(numbers,new3, new, new2, sep='\n')
#
#
#new4 = tuple(filter(lambda x: x > 5, numbers))
#new5 = [i for i in numbers if i > 5]
#
#print(new4, new5, sep='\n')
#
#
#new6 = sorted(numbers, key=lambda x: x % 2 == 0, reverse = True)
#
#print(new6)
#
#result = lambda *args: int(sum(args) / len(args))
#
#print(result(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
#
#try:
#    print(2 + '3')
#except:
#    print('неверный тип данных')
#finally:
#    print('проверка завершена')
#
#
#word = 'Python'
#
#while 1:
#    try :
#        index_user =int(input('введите индекс: '))
#        print(word[index_user])
#
#    except IndexError:
#        print('неверный индекс!')
#
#    except ValueError:
#        print('только цифры!')
#
#    except:
#        print('Oops, Error!')

#file = open('file.txt', 'w', encoding='utf-8')
#file.write('123456789')
#file.close()
#
## 'w' - это запись и перезапись
#
#with open ('file.txt', 'a') as file:
#    file.write('\n987654321')
#
## 'a' - это  add добавить
#
## 'x' - это проверяет файл на сууществование / безконфликный режим создание файла если такого файла нету
#
#
#with open ('file.txt', 'r', encoding='utf-8') as file:
#    for i in file.read():
#        print(i, end='')
    #print(file.read())
    #print(file.readline())
    #print(file.readline())
    #print(file.readlines()[-1])


# 'r' - показывает резултать в терминале
#
#
#name = 'Bogdan'
#print(dir(name))
#


#n = int(input())
#
#b = ''
#
#while n > 0:
#    b = str(n % 2) + b
#    n = n // 2
#
#print(b)
#

#def q (a=1 ,b=1):
#   # n = a + b
#   # w = ''
##
#   # while n > 0:
#   #     w = str(n % 2) + w
#   #     n = n // 2
#    return bin(a+b)[2::]
#
#print(q(24,4))
#
#
# a = 1000
# '''1000 - 7'''
# '''Я гуль'''
# while a >= 0:
#
    # print(f'{a} - 7 = {a-7} ')
    # a -= 7

#
# a = ['a', 'v', 'a', 'e', 'v']
# a = list(dict.fromkeys(a))
# print(a)
