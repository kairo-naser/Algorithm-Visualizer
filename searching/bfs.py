# ============================================================
# BINARY SEARCH ALGORITHM
# ============================================================
# Works on sorted arrays. Cuts the array in half each step.
# ============================================================

def binary_search(arr, target):
    arr = sorted(arr)
    print("\n==============================")
    print("🔎 BINARY SEARCH")
    print("Sorted Array:", arr)
    print("Target:", target)
    print("==============================")
    left, right = 0, len(arr)-1
    step = 1
    while left <= right:
        mid = (left + right)//2
        print(f"\nStep {step}: Left={left}, Right={right}, Mid={mid}, Value={arr[mid]}")
        if arr[mid] == target:
            print("🎯 Target found at index:", mid)
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
        step += 1
    print("❌ Target NOT found")
    return -1

arr = [3, 7, 9, 1, 2, 5]
binary_search(arr, 9)
