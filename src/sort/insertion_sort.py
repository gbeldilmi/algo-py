def insertion_sort(arr):
    l = len(arr)
    for i in range(1, l):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def insertion_sort_recursive(arr, i):
    def insert(arr, j):
        if j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            insert(arr, j - 1)
    l = len(arr)
    if i < l: 
        insert(arr, i)
        insertion_sort_recursive(arr, i + 1)
    return arr


if __name__ == '__main__':
    arr = [5, 3, 1, 4, 2]
    insertion_sort(arr)
    print(arr)  
    arr = [5, 3, 1, 4, 2]
    insertion_sort_recursive(arr, 0)
    print(arr)
