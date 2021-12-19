

# def isHappyRecursion(nums, value):
#     squares = [int(n)**2 for n in str(value)]
#     result = sum(squares)
#     if result == 1:
#         return True
#     elif result in nums:
#         return False
#     nums.append(value)
#     return isHappyRecursion(nums,result)
#
#
# class Solution:
#     def isHappy(self, n):
#         return isHappyRecursion([],n)


class Solution:
    def isHappy(self, n):
        my_set = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in my_set:
                return False
            my_set.add(n)
        return True