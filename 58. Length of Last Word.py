

class Solution:
    def lengthOfLastWord(self, s):

        try:
            return len(s.split()[-1]) if len(s.split()[-1]) > 0 else 0
        except:
            return 0

