def dichotomic_search(arr, val):
    l = len(arr)
    if l == 0:
        return -1
    if l == 1:
        return 0 if arr[0] == val else -1
    m = l // 2
    if arr[m] == val:
        return m
    elif arr[m] > val:
        return dichotomic_search(arr[:m], val)
    else:
        return m + dichotomic_search(arr[m:], val)


if __name__ == '__main__':
    arr = range(10)
    print(dichotomic_search(arr, 3))
    print(dichotomic_search(arr, 7))
