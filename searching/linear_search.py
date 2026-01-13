# ============================================================
# LINEAR SEARCH ALGORITHM
# ============================================================
# Checks each element sequentially until the target is found.
# ============================================================

def linear_search(arr, target):
    print("\n==============================")
    print("🔍 LINEAR SEARCH")
    print("Target:", target)
    print("==============================")
    for i in range(len(arr)):
        print(f"Step {i+1}: Checking index {i}, value = {arr[i]}")
        if arr[i] == target:
            print("🎯 Target found at index:", i)
            return i
    print("❌ Target NOT found")
    return -1

arr = [3, 7, 9, 1, 2, 5]
linear_search(arr, 9)
