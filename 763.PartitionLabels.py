# class Solution:
#     def partitionLabels(self, s):
#         self.result = []
#         self.ht = dict()
#         start = 0
#         back = 0
#         front = 1
#
#         for c in s:
#             if c in self.ht:
#                 self.ht[c] += 1
#             else:
#                 self.ht[c] = 1
#
#         self.ht[s[back]] -= 1
#
#         while front < len(s):
#             self.ht[s[front]] -= 1
#             while back < len(s) and self.ht[s[back]] == 0 and back < front:
#                 back += 1
#             if back == front and back != start:
#                 front += 1
#                 self.result.append(front - start)
#                 back += 1
#                 start = back
#                 continue
#
#             front += 1
#
#         if start < len(s):
#             self.result.append(front - start)
#
#         return self.result
class Solution:
    def partitionLabels(self, s):
        self.ht = dict()
        self.result = []

        for i in range(len(s)):
            self.ht[s[i]] = i

        left = 0
        right = 0
        for idx, c in enumerate(s):
            right = max(right, self.ht[s[idx]])
            if right == idx:
                self.result.append(right - left + 1)
                left = idx + 1

        return self.result


my_solution = Solution()
print(my_solution.partitionLabels("caedbdedda"))