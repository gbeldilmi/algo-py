def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def selection_sort_recursive(arr, i): # Less efficient than the above one
    l = len(arr)
    if i < l:
        min_index = i
        for j in range(i + 1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        selection_sort_recursive(arr, i + 1)
    return arr


if __name__ == '__main__':
    arr = [5, 3, 1, 4, 2]
    selection_sort(arr)
    print(arr)
    arr = [5, 3, 1, 4, 2]
    selection_sort_recursive(arr, 0)
    print(arr)
