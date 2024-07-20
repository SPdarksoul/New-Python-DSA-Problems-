def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to pivot
        right = [x for x in arr if x > pivot]  # Elements greater than pivot
        return quicksort(left) + middle + quicksort(right)

arr = [3, 6, 8, 10, 1, 2, 1]
print("Unsorted array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)


# PS D:\Python  new> & C:/Users/sagar/AppData/Local/Microsoft/WindowsApps/python3.11.exe "d:/Python  new/quicksort.py"
# Unsorted array: [3, 6, 8, 10, 1, 2, 1]
# Sorted array: [1, 1, 2, 3, 6, 8, 10]
# PS D:\Python  new> 
