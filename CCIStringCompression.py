class Solution:
    def compressString(self, s):
        if len(s) < 2:
            return s
        front = back = 0
        ns = ""

        while True:
            while s[front] == s[back]:
                front += 1
                if front == len(s):
                    ns += s[back] + str(front - back)
                    return ns if len(ns) < len(s) else s
            ns += s[back] + str(front - back)
            back = front

my_solution = Solution()
print(my_solution.compressString("aabcccccaaa"))