# ============================================================
# COUNTING SORT ALGORITHM
# ============================================================
# Counting Sort counts occurrences of each element
# and builds sorted array.
# Time Complexity: O(n+k), k = max value
# Space Complexity: O(k)
# ============================================================

data = [64, 34, 25, 12, 22, 11, 90]

def print_result(name, array):
    print("\n" + name)
    print("Sorted Array:", array)

def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for num in arr:
        count[num] += 1
    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1

arr_copy = data.copy()
counting_sort(arr_copy)
print_result("Counting Sort", arr_copy)
