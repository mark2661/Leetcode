class Solution:
    def compress(self, chars):
        if len(chars) < 2:
            return len(chars)
        left = right = 0
        s = ""
        while right < len(chars):
            if chars[right] != chars[left]:
                s += chars[left]
                if right - left > 1:
                    s += str(right - left)
                left = right
            right += 1
        if left < len(chars):
            s += chars[left]
            if right - left > 1:
                s += str(right - left)
        chars = list(s)
        return len(s)

