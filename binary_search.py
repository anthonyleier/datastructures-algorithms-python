def binary_search(array, item, begin=0, end=None):
    if not end:
        end = len(array) - 1

    if begin <= end:
        middle = (begin + end) // 2
        if array[middle] == item:
            return middle

        if item < array[middle]:
            return binary_search(array, item, begin, middle-1)

        if array[middle] < item:
            return binary_search(array, item, middle+1, end)

    return None


if __name__ == "__main__":
    array = [2, 2, 4, 7, 11, 21, 23, 30, 41]
    print(binary_search(array, 11))
