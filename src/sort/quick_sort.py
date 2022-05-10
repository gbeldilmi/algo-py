def quick_sort(arr, low, high):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        c = True
        while c:
            while i <= j and arr[i] <= pivot:
                i += 1
            while j >= i and arr[j] >= pivot:
                j -= 1
            if i > j:
                c = False
            else:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


if __name__ == '__main__':
    arr = [5, 3, 1, 4, 2]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
