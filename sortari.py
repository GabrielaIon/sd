import random
from random import randrange as rand


def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def CountSort(arr):
    n = len(arr)
    out = [0] * n
    c = [0] * 1000000
    for i in arr:
        c[i] += 1
    for i in range(1, 1000000):
        c[i] += c[i - 1]
    for i in arr:
        out[c[i] - 1] = i
        c[i] -= 1
    return out


def Interclasare(lst, ldr):
    i = j = 0

    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] <= ldr[j]:
            rez.append(lst[i])
            i += 1
        else:
            rez.append(ldr[j])
            j += 1

    rez.extend(lst[i:])
    rez.extend(ldr[j:])

    return rez


def MergeSort(ls):
    if len(ls) <= 1:
        return ls
    else:
        mij = len(ls) // 2
        lst = MergeSort(ls[:mij])
        ldr = MergeSort(ls[mij:])
        return Interclasare(lst, ldr)


def partitierandom(arr, st, dr):
    pivot = arr[dr]
    i = st - 1
    for x in range(st, dr):
        if arr[x] <= pivot:
            i += 1
            arr[i], arr[x] = arr[x], arr[i]
    arr[i + 1], arr[dr] = arr[dr], arr[i + 1]
    return i + 1


def QuickSort(arr, st, dr):
    if st < dr:
        p = partitierandom(arr, st, dr)
        QuickSort(arr, st, p - 1)
        QuickSort(arr, p + 1, dr)
    return arr


def radixsort(arr):
    RADIX = 10
    max = False
    temp, poz = -1, 1
    while not max:
        max = True
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            temp = i / poz
            buckets[temp % RADIX].append(i)
            if max and temp > 0:
                max = False
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        poz *= RADIX


def RadixSort_b2(arr, k):
    n = len(arr)
    m = max(arr)
    if 2 ** k > m:
        return arr
    bucket = [[], []]
    for i in range(n):
        c = (arr[i] >> k) & 1
        if c == 0:
            bucket[0].append(arr[i])
        else:
            bucket[1].append(arr[i])
    s = []
    s.extend(bucket[0])
    s.extend(bucket[1])
    return RadixSort_b2(s, k + 1)


def teste(arr):
    ok = 1
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return 0
    return 1


import time
import copy

f = open("sort.in")
nr = int(f.readline())
i = 1
for l in f:
    n = int(l.split()[0])
    m = int(l.split()[1])
    test = open("test.in", "w")
    for j in range(n):
        test.write(str(rand(m)) + " ")
    test.close()

    test = open("test.in", "r")
    lista = []
    lista = test.readline().split()
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    test.close()

    # bubble sort
    start = time.time()
    if len(lista) > 10000:
        print("Nu se poate aplica bubble sort pt aceste numere")
    else:
        sort = copy.deepcopy(lista)
        BubbleSort(sort)
        final = time.time()
        if teste(sort):
            print("Bubble sort pt {} numere mai mici decat {} in {} secunde".format(n, m, final - start))

    # count sort
    start = time.time()
    sort = CountSort(lista)
    final = time.time()
    if teste(sort) == 0:
        print("Nu se poate aplica count sort pt aceste numere")
        if final - start > 5:
            print("dureaza prea mult.")
    else:
        print("Counting sort pt {} numere mai mici decat {} in {} secunde".format(n, m, final - start))

    # merge sort
    start = time.time()
    sort = MergeSort(lista)
    final = time.time()
    if teste(sort) == 0:
        print("Nu se poate aplica merge sort pt aceste numere")
        if final - start > 5:
            print("dureaza prea mult.")
    else:
        print("Merge sort pt {} numere mai mici decat {} in {} secunde".format(n, m, final - start))

    # quicksort
    sort = copy.deepcopy(lista)
    start = time.time()
    sort = QuickSort(sort, 0, n - 1)
    final = time.time()
    if teste(sort) == 0:
        print("Nu se poate aplica quick sort pt aceste numere")
        if final - start > 5:
            print("dureaza prea mult.")
    else:
        print("Quick sort pt {} numere mai mici decat {} in {} secunde".format(n, m, final - start))

    # radix sort b2
    start = time.time()
    s = RadixSort_b2(lista, 0)
    final = time.time()
    if teste(s) == 0:
        print("Nu se poate aplica radix sort pt aceste numere")
        if final - start > 5:
            print("dureaza prea mult.")
    else:
        print("Radix sort pt {} numere mai mici decat {} in {} secunde".format(n, m, final - start))

    # sort
    start = time.time()
    s = sorted(lista)
    final = time.time()
    if teste(s):
        print("Sort pentru {} numere mai mici decat {}: {} secunde".format(n, m, final - start))
