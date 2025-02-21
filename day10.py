def bubble_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j + 1] = l[j+1], l[j]
            #print(j, end=' ')
    return l


print(bubble_sort([33, 8, -11, 9, 1]))