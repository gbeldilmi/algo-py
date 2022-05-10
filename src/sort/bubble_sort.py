def bubble_sort(arr):
    l = len(arr)
    sorted = False
    i = 1
    while not sorted:
        sorted = True
        for j in range(l-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        i += 1
    return arr


if __name__ == '__main__':
    arr = [5, 3, 1, 4, 2]
    bubble_sort(arr)
    print(arr)
