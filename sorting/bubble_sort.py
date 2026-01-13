# ============================================================
# BUBBLE SORT ALGORITHM
# ============================================================
# Bubble Sort repeatedly swaps adjacent elements if they are
# in the wrong order.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# ============================================================

data = [64, 34, 25, 12, 22, 11, 90]

def print_result(name, array):
    print("\n" + name)
    print("Sorted Array:", array)

def bubble_sort(arr):
    """
    Sorts an array in ascending order using Bubble Sort.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr_copy = data.copy()
bubble_sort(arr_copy)
print_result("Bubble Sort", arr_copy)
