
def bubble_sort(bubble):
    n = len(bubble)
    while bubble != sorted(bubble):
        for p in range(0, n-1):
            if bubble[p] > bubble[p+1]:
                bubble[p], bubble[p+1] = bubble[p+1], bubble[p]


bubble = [13, 3, 56, 0, 71, 96, 35, 8, 9, 27, 48, 82]
bubble_sort(bubble)
bubble_list = bubble
print(bubble_list)



from random import randint
n = 5000
ResultOK = False
first = 0
last = n - 1
pos = 0
def binary_search (val) :
    global ResultOK, first, last, pos
    while first < last:
        middle =(first + last) // 2
        if val == middle:
            first = middle
            last = first
            ResultOK = True
            pos = middle
            break
        elif val > middle:
            first = middle+1
        else:
            last = middle - 1

    if ResultOK == True:
        print('Элемент найден')
        print(pos)
    else:
        print("Элемент не найден")

val =  randint(first, n)
print(val)
binary_search(val)
