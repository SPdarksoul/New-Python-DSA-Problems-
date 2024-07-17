def SelectionSort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n):
        findex = i  # Initialize findex to the current index
        for j in range(i + 1, n):
            if arr[j] < arr[findex]:
                findex = j
        # Swap the found minimum element with the first element
        arr[findex], arr[i] = arr[i], arr[findex]

arr = [4, 33, 12, 1, 565]
SelectionSort(arr)
print(arr)


def SelectionSort(arr: list[int]) -> None:
    n = len(arr)
    for j in range(n):
        findex = j  # Initialize findex to the current index
        for i in range(j - 1, n):
            if arr[j] < arr[findex]:
                findex = i
        # Swap the found minimum element with the first element
        arr[findex], arr[i] = arr[i], arr[findex]

arr = [4, 33, 12, 1, 565]
SelectionSort(arr)
print(arr)
