#Definition for singly-linked list.
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        stack = deque()
        current = head

        while current != None:
            stack.append(current)
            current = current.next

        current = head
        while len(stack) > 0:
            top_of_stack = stack.pop()
            if top_of_stack.val != current.val:
                return False
            current = current.next

        return True

ll = ListNode(1,ListNode(2))
my_solution = Solution()
print(my_solution.isPalindrome(ll))


