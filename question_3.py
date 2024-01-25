# Данный алгоритм в худшем случае выполняется за О(n^2), но в большестве случаев
# это не так, и среднее время выполнене алгорима О(n log n).
# Так же данный алгорит более эффектвен на больших массивах нежели функция sorted
def quick_sort_in_place(array: list, left: int, right: int):
    center = (left + right) // 2
    pivot = array[center]
    i, j = left, right
    if left >= right:
        return
    while i < j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_sort_in_place(array, left, j)
    quick_sort_in_place(array, i, right)
    return array


if __name__ == '__main__':
    pass
