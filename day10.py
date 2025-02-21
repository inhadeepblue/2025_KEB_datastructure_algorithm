import time
import random

def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e - s}초')
        return r
    return wrapper


@time_decorator
def insertion_sort(l):
    for i in range(1, len(l)):
        value = l[i]
        while i > 0 and l[i-1] > value:
            l[i] = l[i-1]
            i = i - 1
            #print(i, end=' ')
        l[i] = value
    return l


@time_decorator
def bubble_sort(l):
    for i in range(len(l) - 1):
        no_swap = True
        for j in range(len(l) - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j + 1] = l[j+1], l[j]
                no_swap = False
                #print(j, end=' ')
        if no_swap:
            return l
    return l


def quick_sort(l):
    n = len(l)
    if n<=1: return l
    pivot = l[n//2]
    left, right = list(), list()

    for i in l:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)

    return quick_sort(left)+[pivot]+quick_sort(right)


lists1 = [random.randint(1, 100000) for _ in range(10000)]
lists2 = lists1.copy()
lists3 = lists1.copy()
bubble_sort(lists1)
insertion_sort(lists2)

s = time.time()
quick_sort(lists3)
e = time.time()
print(f'실행시간 : {e - s}초')