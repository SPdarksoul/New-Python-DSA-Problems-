def search(arr, target):
    n = len(arr)
    s, e = 0, n - 1
    while s <= e:
        mid = (s + e) // 2
        if target < arr[mid]:
            e = mid - 1
        elif target > arr[mid]:
            s = mid + 1
        else:
            return mid
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
result = search(arr, 4)
print(result)
