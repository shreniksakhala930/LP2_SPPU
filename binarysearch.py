def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid   # element found, return index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1   # element not found


# Example usage
numbers = [1, 3, 5, 7, 9, 11]
result = binary_search(numbers, 7)
print("\n The Array is [ 1,3,5,7,9,11] ")
print("\n The answer of binary search is :\n")

print("Index:", result)
