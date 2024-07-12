def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track whether any swaps have been made
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps were made, the array is already sorted
        if not swapped:
            break

# Taking input from the user
input_array = list(map(int, input("Enter the elements of the array (space-separated): ").split()))

# Performing bubble sort
bubble_sort(input_array)

print("Sorted array is:")
print(input_array)