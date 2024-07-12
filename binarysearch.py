def binary_search(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2

        # Check if the element is present at the middle
        if arr[mid] == x:
            return mid

        # If the element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, right, x)

    else:
        # Element is not present in array
        return -1

# Taking input from the user
input_array = list(map(int, input("Enter the elements of the array (space-separated and sorted): ").split()))
search_element = int(input("Enter the element to search for: "))

# Performing binary search
result = binary_search(input_array, 0, len(input_array) - 1, search_element)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
