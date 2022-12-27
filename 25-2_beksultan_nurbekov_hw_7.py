from random import randint, choice

k = []
for i in range(12):
    k.append(randint(0, 100))
print(f'unsorted list: {k}')
def buble_sort(ls:list):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1], ls[j]
    return ls
value = choice(buble_sort(k))
print(f'desired number: {value}')
print(f'sorted list: {k}')
def bynary_search(value: int, ls: list):
    # result = False
    first = 0
    last = len(ls)
    # print(last)
    while True:
        if first < last:
            middle = (first + last) // 2
            if value == ls[middle]:
                print('i found the number i was looking for')
                first = middle
                last = first
                pos = middle
                print(f'position:{pos}')
                break
            elif value > ls[middle]:
                first = middle + 1
            elif value < ls[middle]:
                last = middle - 1
        else:
            print('element not found')
            break

bynary_search(value, k)



unsorted_list = []
for i in range(11):
    unsorted_list.append(randint(1, 99))

def selection_sort(ls: list):
    for i in range(len(ls)):
        min_val = ls[i]
        for j in range(len(ls) - i):
            if i < min_val:
                min_val = i
        ls[i], ls[min_val] = ls[min_val], ls[i]
    return ls
print(f'\nunsorted list:{unsorted_list}')
print(f'sorted (list selection sort):{selection_sort(unsorted_list)}')

