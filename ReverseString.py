class Solution:
    def reverseString(self, s):
      front_idx = 0
      back = len(s) - 1

      while front_idx < back:
          temp_value = s[front_idx]
          s[front_idx] = s[back]
          s[back] = temp_value

          front_idx += 1
          back -= 1