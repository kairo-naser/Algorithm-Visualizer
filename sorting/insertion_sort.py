# ============================================================
# INSERTION SORT ALGORITHM
# ============================================================
# Insertion Sort builds a sorted portion by inserting each
# element into its correct position.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# ============================================================

data = [64, 34, 25, 12, 22, 11, 90]

def print_result(name, array):
    print("\n" + name)
    print("Sorted Array:", array)

def insertion_sort(arr):
    """
    Sorts an array in ascending order using Insertion Sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]   # Current element
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr_copy = data.copy()
insertion_sort(arr_copy)
print_result("Insertion Sort", arr_copy)
