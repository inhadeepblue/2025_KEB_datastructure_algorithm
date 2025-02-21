def insertion_sort(l):
    for i in range(1, len(l)):
        value = l[i]
        while i > 0 and l[i-1] > value:
            l[i] = l[i-1]
            i = i - 1
            print(i, end=' ')
        l[i] = value
    return l


def bubble_sort(l):
    for i in range(len(l) - 1):
        no_swap = True
        for j in range(len(l) - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j + 1] = l[j+1], l[j]
                no_swap = False
                print(j, end=' ')
        if no_swap:
            return l
    return l


print(bubble_sort([33, 8, -11, 9, 1]))
print(bubble_sort([13, 15, 20, 99, 100]))
print(insertion_sort([33, 8, -11, 9, 1]))
print(insertion_sort([13, 15, 20, 99, 100]))