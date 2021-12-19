class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        result = []
        front = 10
        back = 0
        st = s[back:front]
        seq_set = set()
        set.add(st)
        while front < len(s):
            st = st[1:] + s[front]
            if st in seq_set:
                result.append()
