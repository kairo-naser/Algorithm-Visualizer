# ============================================================
# QUICK SORT ALGORITHM
# ============================================================
# Quick Sort picks a pivot and partitions the array around it.
# Recursively sorts partitions.
# Time Complexity: O(n log n) average
# Space Complexity: O(log n)
# ============================================================

data = [64, 34, 25, 12, 22, 11, 90]

def print_result(name, array):
    print("\n" + name)
    print("Sorted Array:", array)

def quick_sort(arr):
    """
    Sorts an array in ascending order using Quick Sort.
    Returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

arr_copy = data.copy()
arr_sorted = quick_sort(arr_copy)
print_result("Quick Sort", arr_sorted)
