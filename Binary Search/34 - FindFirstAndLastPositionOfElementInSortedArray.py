def searchRange(nums, target):
    def findFirst():
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                right = mid - 1  # search left part
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

    def findLast():
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                left = mid + 1  # search right part
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

    return [findFirst(), findLast()]
