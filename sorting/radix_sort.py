# ============================================================
# RADIX SORT ALGORITHM
# ============================================================
# Radix Sort processes digits of numbers starting from LSB
# to MSB using Counting Sort as subroutine.
# Time Complexity: O(d*(n+k)), d=digits, k=max digit
# Space Complexity: O(n+k)
# ============================================================

data = [64, 34, 25, 12, 22, 11, 90]

def print_result(name, array):
    print("\n" + name)
    print("Sorted Array:", array)

def counting_sort_by_digit(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10
    for i in range(len(arr)):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = len(arr) - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

arr_copy = data.copy()
radix_sort(arr_copy)
print_result("Radix Sort", arr_copy)
