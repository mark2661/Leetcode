

class Solution:

    # def __init__(self):
    #     self.my_stack = self.Stack()

    class Stack:

        stack = []

        def push(self,value):
            self.stack.append(value)

        def pop(self):
            return self.stack.pop()

        def peak(self):
            return self.stack[-1]

        def size(self):
            return len(self.stack)

        def empty(self):
            return len(self.stack) == 0

        def clear(self):
            self.stack.clear()


    def isValid(self, s):

        if len(s) < 2:
            return False

        self.Stack.clear(self.Stack)

        bracket_dictionary = {")":"(","}":"{","]":"["}

        for bracket in s:

            # If stack is empty and you come across an open bracket the string is False
            if bracket in bracket_dictionary.keys() and self.Stack.empty(self.Stack):
                return False

            # If open bracket push it on the stack
            if bracket in bracket_dictionary.values():
                self.Stack.push(self.Stack,bracket)

            #If closing bracket compare with the value on the top of the stack
            else:
                if bracket_dictionary[bracket] == self.Stack.peak(self.Stack):
                    self.Stack.pop(self.Stack)
                else:
                    return False
        return self.Stack.empty(self.Stack)

my_solution = Solution()
print(my_solution.isValid("(]"))
print(my_solution.isValid("([)]"))
print(my_solution.isValid("{[]}"))