
# def combo_sum(candidates,target,solutions, s=[], st=set()):
#     if target < 0:
#         return
#     if target == 0:
#         s.sort()
#         if tuple(s) not in st:
#             solutions.append(s)
#             st.add(tuple(s))
#         return
#     temp_s = s.copy()
#     for candidate in candidates:
#         temp_s.append(candidate)
#         combo_sum(candidates, target - candidate, solutions, temp_s, st)
#         temp_s = s.copy()




class Solution:
    def combinationSum(self, candidates, target):
        self.res = []
        self.candidates = candidates
        self.backtrack([], target, 0)
        return self.res

    def backtrack(self, path, target, idx):
        if target == 0:
            self.res.append(path)
            return
        if target < 0:
            return

        for i in range(idx, len(self.candidates)):
            self.backtrack(path + [self.candidates[i]], target - self.candidates[i], i)

my_solution = Solution()
print(my_solution.combinationSum([2,3,6,7],7))
print(my_solution.combinationSum([2,3,5],8))
print(my_solution.combinationSum([1,2],1))