



class Solution:
    def majorityElement(self, nums):
        my_dict = dict()
        x = len(nums) // 2

        for number in nums:
            if my_dict.get(number) != None:
                my_dict[number] = my_dict[number] + 1
            else:
                my_dict[number] = 1

        for key in my_dict.keys():
            if my_dict[key] > x:
                return key

