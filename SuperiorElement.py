def superiorElement(arr: list[int]) -> list[int]:
    n = len(arr)
    i = n - 1
    ans = []
    mx = -float('inf')
    while i >= 0:
        if arr[i] > mx:
            ans.append(arr[i])
            mx = arr[i]
        i -= 1  # Move this line inside the loop
    return ans

arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(superiorElement(arr))
