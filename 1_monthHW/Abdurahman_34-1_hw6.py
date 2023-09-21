print("Home Work №6\n")


def multiplication_number(*args):
    '''Перемноежения чисел - каждая последуящая число умнажается на другую
Пример: (2, 3, 4, 5) => 2*3*4*5 == 120'''
    number = args[0]
    for i in args[1::]:
        number *= i
    return number


print(multiplication_number.__doc__)

enternumber = input('Введите числа через пробел: ') # Однаразовая штука
number2 = [int(i) for i in enternumber.split()]
result = multiplication_number(*number2)
print(result)
print(multiplication_number(2, 3, 4, 5)) # => 120


print()


def palindrome(word= "hello"):
    '''Палиндром (Palindrome) - Зеркальная строка, которая читается одинаково вперед и назад
Пример: "дед", "шалаш"...'''
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False

def palindrome(word = 'Hello'):
    word = word.replace('', '')
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome.__doc__)

enterword = input('Введите слово: ') # Одноразовая
print(palindrome(enterword))
print(palindrome()) # False / потому что 'hello' не палиндром
print(palindrome("1221")) # True


print()


def calculator (number1: int, operator: str, number2: int):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '/':
        return number1 / number2
    elif operator == '*':
        return number1 * number2
    elif operator == '**':
        return number1 ** number2
    elif operator == '//':
        return number1 // number2
    elif operator == '%':
        return number1 % number2

print(calculator(2,'**', 3))
print(calculator(5,'+', 9.6))
print(calculator(20,'%', 3))
print(calculator(30,'-', 3))
print(calculator(27,'*', 4))
print(calculator(121,'//', 11))
print(calculator(28,'/', 5))
