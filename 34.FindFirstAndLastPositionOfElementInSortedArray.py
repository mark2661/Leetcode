class Solution:
    def searchRange(self, nums, target):
        self.nums = nums
        def BS(start, end, target):
            while start <= end:
                mid = (start + end) // 2
                if self.nums[mid] == target:
                    return mid
                if self.nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        if not self.nums:
            return [-1,-1]

        min_idx = max_idx = BS(0, len(nums) - 1, target)
        if min_idx == -1:
            return [-1,-1]

        while True:
            i = BS(0, min_idx - 1, target)
            if i == -1:
                break
            min_idx = i

        while True:
            i = BS(max_idx + 1, len(nums) - 1, target)
            if i == -1:
                break
            max_idx = i

        return [min_idx, max_idx]
