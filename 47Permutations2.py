def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    first = nums[0]
    rest = nums[1::]
    withoutFirst = permute(rest)
    withFirst = []
    for permutation in withoutFirst:
        for i in range(len(permutation) + 1):
            new_permutation = permutation.copy()
            new_permutation.insert(i, first)
            withFirst.append(new_permutation)
    return withFirst


def removeDuplicates(permutations):
    t = [tuple(n) for n in permutations]
    s = set(t)
    return [list(n) for n in s]

class Solution:
    def permuteUnique(self, nums):
        return removeDuplicates(permute(nums))


my_solution = Solution()
print(my_solution.permuteUnique([1,1,2]))
print(my_solution.permuteUnique([1,2,3]))