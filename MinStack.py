
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []


    def push(self, x):
        self.stack.append(x)
        if len(self.minstack) == 0:
            self.minstack.append(x)
        elif x <= self.minstack[-1]:
            self.minstack.append(x)


    def pop(self):
        if self.stack[-1] == self.minstack[-1]:
            del self.minstack[-1]

        return self.stack.pop(-1)

    def top(self):
        return self.stack[-1]


    def getMin(self):
        return self.minstack[-1]