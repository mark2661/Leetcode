

# class Solution:
#     def isPalindrome(self, x):
#         try:
#             return x == int(str(x)[-1::-1])
#         except:
#             return False

class Solution:
    """
        // Special cases:
        // As discussed above, when x < 0, x is not a palindrome.
        // Also if the last digit of the number is 0, in order to be a palindrome,
        // the first digit of the number also needs to be 0.
        // Only 0 satisfy this property.
    """
    def isPalindrome(self, x):
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        reverse = 0
        while(x > reverse):
            """
            Before we add a new number to the end i.e x % 10 we must first shift the numbers in reverse up by a unit 
            e.g if reversed = 9 and we want to add 4 to make 94 we must first shift 9 up a unit to 90 and then add 4
            """
            reverse = reverse * 10 + x % 10
            x /= 10

        return x == reverse or x == reverse / 10

my_solution = Solution()
print(my_solution.isPalindrome(121))
print(my_solution.isPalindrome(-121))
print(my_solution.isPalindrome(10))
print(my_solution.isPalindrome(-101))