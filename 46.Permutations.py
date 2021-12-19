
def permuateArr(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    firstElm = nums[0]
    rest = nums[1:]
    permutaionsWithoutFirst = permuateArr(rest)
    permutationsWithFirst = []

    for perm in permutaionsWithoutFirst:
        for i in range(len(perm) + 1):
            temp = perm.copy()
            temp.insert(i,firstElm)
            permutationsWithFirst.append(temp)

    return permutationsWithFirst


class Solution:
    def permute(self, nums):
        return permuateArr(nums)



my_solution = Solution()
print(my_solution.permute([1,2,3]))
print(my_solution.permute([0,1]))
print(my_solution.permute([1]))
