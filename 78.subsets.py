
# def find_subsets(n, state, rem, result=[]):
#     if len(state) == n or len(rem) == 0:
#         result.append(tuple(state))
#         return result
#     result.append(tuple(state))
#     temp_rem = rem.copy()
#     temp_state = state.copy()
#     i = 0
#     while len(rem) > 0:
#         temp_state.append(rem[i])
#        # if valid(temp_state):
#         temp_rem.remove(rem[i])
#         find_subsets(n, temp_state, temp_rem, result)
#         rem.remove(rem[i])
#         temp_rem = rem.copy()
#         temp_state = state.copy()
#     return result
#
# def format(result):
#     return [list(n) for n in result]

class Solution:
    def subsets(self, nums):
        self.result = []
        self.nums = nums
        self.backtrack(len(nums), [], 0)
        return self.result

    def backtrack(self, n, state, idx):
        if idx > len(self.nums):
            return
        self.result.append(state)

        for i in range(idx, len(self.nums)):
            self.backtrack(n, state + [self.nums[i]], i + 1)



my_solution = Solution()
print(my_solution.subsets([1,2,3]))
print(my_solution.subsets([0]))