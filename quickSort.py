def quickSort(array):
    length = len(array)

    if length <= 1:
        return array
    else:
        pivot = array.pop()

        greater_elements = []
        lower_elements = []

        for element in array:
            if element > pivot:
                greater_elements.append(element)
            else:
                lower_elements.append(element)

        return quickSort(lower_elements) + [pivot] + quickSort(greater_elements)

print(quickSort([4, 2, 1, 6, 3]))
