def searchInsert(arr: [int], target: int) -> int:
    n = len(arr)
    if n == 0:
        return 0
    ans = n
    s, e = 0, n - 1

    while s <= e:
        mid = (s + e) // 2
        if arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
            ans = mid
    return ans


arr = [1, 2, 3, 4, 5, 6, 7]
result = searchInsert(arr, 2)
print(result)