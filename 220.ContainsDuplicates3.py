class Solution:
    def containsNearbyAlmostDuplicate(self, nums ,k , t):
        def valid(i, j):
            return abs(nums[i] - nums[j]) <= t and abs(i - j) <= k and i != j
        front = 0
        back = 0

        while front < len(nums):
            if valid(front, back):
                return True
            if abs(front - back) > k or (front == len(nums) -1 and back < front):
                back += 1
                continue
            else:
                front += 1
        return False


my_solution = Solution()
print(my_solution.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
print(my_solution.containsNearbyAlmostDuplicate([1,0, 1, 1], 1, 2))
print(my_solution.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
print(my_solution.containsNearbyAlmostDuplicate([1,2,1,1], 1, 0))
print(my_solution.containsNearbyAlmostDuplicate([1,2,2,3,4,5], 3, 0))
