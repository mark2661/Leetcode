
class Solution:
    def characterReplacement(self, s, k):
        self.s = s
        self.k = k
        self.max_l = 0
        front = 0
        back = 0
        self.ht = {chr(i+64):0 for i in range(1,27)}

        while front < len(s):
            self.ht[s[front]] += 1

            while (front - back + 1 - self.getMaxCount()) > k:
                self.ht[s[back]] -= 1
                back += 1

            self.max_l = max(self.max_l, front - back + 1)
            front += 1
        return self.max_l

    def getMaxCount(self):
        max_count = 0
        for key in self.ht.keys():
            if self.ht[key] > max_count:
                max_count = self.ht[key]
        return max_count


my_solution = Solution()
print(my_solution.characterReplacement("ABAB",2))
print(my_solution.characterReplacement("AABABBA",1))
print(my_solution.characterReplacement("ABCDE",1))
print(my_solution.characterReplacement("BAAA",0))