counter = 0


# linear search:
def linear_search(array, item):
    global counter
    for i in range(len(array)):
        counter += 1
        if array[i] == item:
            return i
    return -1


# binary search:
def binary_search(array, item, begin, end):
    global counter
    counter += 1
    if begin == end:
        if array[begin] == item:
            return begin
        else:
            return -1
    mid = (begin + end) // 2
    if item <= array[mid]:
        return binary_search(array, item, begin, mid)
    else:
        return binary_search(array, item, mid + 1, end)


# ternary search:
def ternary_search(array, item, begin, end):
    global counter
    counter += 1
    if end - begin >= 0:
        mid1 = begin + (end - begin) // 3
        mid2 = end - (end - begin) // 3
        if array[mid1] == item:
            return mid1
        if array[mid2] == item:
            return mid2
        if item < array[mid1]:
            return ternary_search(array, item, begin, mid1 - 1)
        elif item > array[mid2]:
            return ternary_search(array, item, mid2 + 1, end)
        else:
            return ternary_search(array, item, mid1 + 1, mid2 - 1)
    return -1
