class Solution:
    def rotateString(self, s, goal):
        if s == goal:
            return True

        original = list(s)
        goal = list(goal)
        s = list(s)

        c = s.pop(0)
        s.append(c)

        while s != original:
            if s == goal:
                return True
            c = s.pop(0)
            s.append(c)
        return False
