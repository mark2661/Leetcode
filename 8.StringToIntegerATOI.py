class Solution:
    def myAtoi(self, s):
        if len(s) == 0:
            return 0
        mf = 1
        val = 0
        pointer = 0
        while pointer < len(s) and s[pointer] == " ":
            pointer += 1
        if pointer >= len(s):
            return 0
        if s[pointer] == "-":
            mf = -1
            pointer += 1
        elif s[pointer] == "+":
            pointer += 1
        while pointer < len(s) and 0 <= ord(s[pointer]) - 48 <= 9:
            val = (val * 10) + ord(s[pointer]) - 48
            pointer += 1
        val *= mf
        if val < pow(-2,31):
            return pow(-2,31)
        elif val > pow(2,31) - 1:
            return pow(2,31) - 1
        else:
            return val