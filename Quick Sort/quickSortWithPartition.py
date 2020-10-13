array = [4, 2, 1, 6, 3]
p = 0
r = len(array) - 1


def partition(array, p, r):
    x = array[r]
    i = p - 1

    for j in range(p, r):
        if(array[j] <= x):
            i = i + 1
            temp1 = array[i]
            array[i] = array[j]
            array[j] = temp1

    temp2 = array[i + 1]
    array[i + 1] = array[r]
    array[r] = temp2

    return i + 1


def quickSort(array, p, r):
    if(p <= r):
        q = partition(array, p, r)
        quickSort(array, p, q - 1)
        quickSort(array, q + 1, r)

    return array


print(quickSort(array, p, r))
