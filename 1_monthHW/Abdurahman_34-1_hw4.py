print("Home Work №4\n")


data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters, numbers = [], []


for i in data_tuple:
    if type(i) == int or type(i) == float:
        numbers.append(i)
    else:
        letters.append(i)

numbers.pop(0)
true = letters.pop(4)
letters.append(true)

numbers.insert(1, 2)

numbers.sort()
letters.reverse()

letters[1] = 'G'
letters[-2] = 'c'

numbers = [i**2 for i in numbers]

print(tuple(letters))
print(tuple(numbers))
