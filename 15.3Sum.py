class Solution:
    def threeSum(self, nums):

        self.result = []

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i-1] and i != 0:
                continue
            j, k = i+1, len(nums)-1
            goal = -nums[i]
            while j < k:
                sum = nums[j] + nums[k]
                if sum > goal:
                    k -= 1
                elif sum < goal:
                    j += 1
                else:
                    self.result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

        return self.result

