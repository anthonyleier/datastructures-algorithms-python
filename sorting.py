def bubblesort(array):
    n = len(array)-1

    for j in range(n):
        for i in range(n):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]


def insertionsort(array):
    n = len(array)

    for i in range(1, n):
        key = array[i]
        j = i-1

        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key


def selectionsort(array):
    n = len(array)

    for j in range(n-1):
        lowest_index = j

        for i in range(j, n):
            if array[i] < array[lowest_index]:
                lowest_index = i

        if array[j] > array[lowest_index]:
            array[j], array[lowest_index] = array[lowest_index], array[j]


def mergesort(array, start=0, end=None):
    if not end:
        end = len(array)

    if (end - start > 1):
        middle = (end + start) // 2
        mergesort(array, start, middle)
        mergesort(array, middle, end)
        merge(array, start, middle, end)


def merge(array, start, middle, end):
    left = array[start:middle]
    right = array[middle:end]
    top_left, top_right = 0, 0

    for k in range(start, end):
        if top_left >= len(left):
            array[k] = right[top_right]
            top_right += 1

        elif top_right >= len(right):
            array[k] = left[top_left]
            top_left += 1

        elif left[top_left] < right[top_right]:
            array[k] = left[top_left]
            top_left += 1

        else:
            array[k] = right[top_right]
            top_right += 1


def quicksort(array, start=0, end=None):
    if not end:
        end = len(array) - 1

    if start < end:
        pivot = partition(array, start, end)
        quicksort(array, start, pivot-1)
        quicksort(array, pivot+1, end)


def partition(array, start, end):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i
