# ============================================================
# SELECTION SORT ALGORITHM
# ============================================================
# Selection Sort repeatedly selects the smallest element from
# the unsorted portion and moves it to the beginning.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# ============================================================

# -------------------------
# SAMPLE DATA
# -------------------------
data = [64, 34, 25, 12, 22, 11, 90]

# -------------------------
# FUNCTION TO PRINT RESULTS
# -------------------------
def print_result(name, array):
    print("\n" + name)
    print("Sorted Array:", array)

# -------------------------
# SELECTION SORT FUNCTION
# -------------------------
def selection_sort(arr):
    """
    Sorts an array in ascending order using Selection Sort.
    """
    for i in range(len(arr)):
        min_index = i  # Assume first unsorted element is min
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j  # Update min_index if smaller element found
        # Swap current element with min element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# -------------------------
# RUN ALGORITHM
# -------------------------
arr_copy = data.copy()
selection_sort(arr_copy)
print_result("Selection Sort", arr_copy)
