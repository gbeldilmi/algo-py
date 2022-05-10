def merge_sort(arr):
    def merge(left, right):
        i, j = 0, 0
        lright = len(right)
        lleft = len(left)
        arr = []
        while i < lleft and j < lright:
            if left[i] < right[j]:
                arr.append(left[i])
                i += 1
            else:
                arr.append(right[j])
                j += 1
        if i < lleft:
            arr.extend(left[i:])
        if j < lright:
            arr.extend(right[j:])
        return arr
    l = len(arr)
    if l <= 1:
        return arr
    m = l // 2
    return merge(merge_sort(arr[:m]), merge_sort(arr[m:]))


if __name__ == '__main__':
    arr = [5, 3, 1, 4, 2]
    print(merge_sort(arr))
    print(arr)
