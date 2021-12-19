

class Solution:
    def romanToInt(self, s):
        roman_numerals_precedence = ("M","D","C","L","X","V","I")
        roman_numerals_values = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        sum = 0

        i = 0
        while (i < len(s)):
            j = i + 1
            if i == len(s) - 1:
                sum += roman_numerals_values[s[i]]
            elif roman_numerals_precedence.index(s[j]) < roman_numerals_precedence.index(s[i]):
                sum += abs(roman_numerals_values[s[i]] - roman_numerals_values[s[j]])
                i += 2
                continue
            else:
                sum += roman_numerals_values[s[i]]
            i += 1
        return sum

my_solution = Solution()
print(my_solution.romanToInt("MCMXCIV"))
print(my_solution.romanToInt("III"))
print(my_solution.romanToInt("IV"))
print(my_solution.romanToInt("LVIII"))
