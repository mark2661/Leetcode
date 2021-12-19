
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
#     temp_c = candidates.copy()
#     for candidate in candidates:
#         temp_s.append(candidate)
#         temp_c.remove(candidate)
#         combo_sum(temp_c, target - candidate, solutions, temp_s, st)
#         temp_s = s.copy()




class Solution:
    def combinationSum2(self, candidates, target):
        self.res = []
        self.candidates = candidates
        self.candidates.sort()
        self.backtrack([], target, 0)
        return self.res

    def backtrack(self, path, target, idx):
        if target == 0:
            self.res.append(path)
            return
        if target < 0:
            return

        for i in range(idx, len(self.candidates)):
            if(i == idx or self.candidates[i] != self.candidates[i-1]):
                self.backtrack(path + [self.candidates[i]], target - self.candidates[i], i+1)

my_solution = Solution()
print(my_solution.combinationSum2([10,1,2,7,6,1,5], 8))
print(my_solution.combinationSum2([2,5,2,1,2], 5))

