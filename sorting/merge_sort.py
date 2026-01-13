# ============================================================
# MERGE SORT ALGORITHM
# ============================================================
# Merge Sort uses divide-and-conquer to split array into
# halves, sort them recursively, and merge them.
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# ============================================================

data = [64, 34, 25, 12, 22, 11, 90]

def print_result(name, array):
    print("\n" + name)
    print("Sorted Array:", array)

def merge_sort(arr):
    """
    Sorts an array in ascending order using Merge Sort.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr_copy = data.copy()
merge_sort(arr_copy)
print_result("Merge Sort", arr_copy)
