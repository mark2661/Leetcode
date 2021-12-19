# class Solution:
#     def reverseWords(self, s):
#         lst = s.split()
#         print(lst)
#         l = 0
#         r = len(lst) - 1
#
#         while l < r:
#             lst[l], lst[r] = lst[r], lst[l]
#             l += 1
#             r -= 1
#         return " ".join(lst)
#
# my_solution = Solution()
# print(my_solution.reverseWords("the sky is blue"))

class Solution:
    def reverseWords(self, s):
        start = 0
        end = len(s) - 1
        while s[start] == " ":
            start += 1
        while s[end] == " ":
            end -= 1
        s = s[start:end+1]
        front = len(s) - 1
        back = len(s)
        ns = ""

        while front > 0:
            if s[front] == " ":
                ns += s[front+1:back] + " "
                while s[front] == " ":
                    front -= 1
                back = front + 1
            else:
                front -= 1

        if back > 0:
            ns += s[front:back]
        return ns



my_solution = Solution()
print(my_solution.reverseWords("the sky is blue"))
print(my_solution.reverseWords(" hello world "))