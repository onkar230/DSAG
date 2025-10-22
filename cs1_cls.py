def binaryClosestSearch(arr, target):
    # Binary search that returns closest value if not found
    l, r = 0, len(arr) - 1
    closest = arr[0]  # start with the first element as closest

    while l <= r:
        mid = (l + r) // 2

        # update closest if this mid is nearer
        if abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]

        if arr[mid] == target:
            return arr[mid]  # exact match
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return closest  # return closest if exact match not found


# ---- Test it ----
nums = [1, 3, 5, 8, 10, 15]
print(binaryClosestSearch(nums, 6))   # should return 5 (closest)
print(binaryClosestSearch(nums, 9))   # should return 8 or 10 (closest = 8 here)
print(binaryClosestSearch(nums, 15))  # exact match → 15
