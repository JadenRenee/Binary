def binary_search(arr, k):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == k:
            result = mid
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Example usage:
arr1 = [1, 2, 3, 4, 5]
k1 = 4
print(binary_search(arr1, k1))  # Output: 3

arr2 = [11, 22, 33, 44, 55]
k2 = 445
print(binary_search(arr2, k2))  # Output: -1
