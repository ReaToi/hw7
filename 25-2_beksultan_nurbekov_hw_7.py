import random

k = []
for i in range(11):
    k.append(random.randint(0, 100))
print(f'unsorted list: {k}')
def buble_sort(ls:list):
    for i in range(len(ls) - 1):
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i],ls[i+1] = ls[i+1], ls[i]
    return ls
value = random.choice(buble_sort(k))
print(f'desired number: {value}')
print(f'sorted list: {k}')
def bynary_search(value: int, ls: list):
    result = False
    first = len(ls) - len(ls)
    last = len(ls)
    # print(last)
    while True:
        if first < last:
            middle = (first + last) // 2
            if value == ls[middle]:
                first = middle
                last = first
                result = True
                print('i found the number i was looking for')
                break
            elif value > ls[middle]:
                first = middle + 1
            elif value < ls[middle]:
                last = middle - 1
        elif result == True:
            print('i found the number i was looking for')
            break
        else:
            print('element not found')
            break

bynary_search(value, k)

