# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        hs = set()
        current = head

        while current:
            if current.next and current.next in hs:
                return current.next
            hs.add(current)
            current = current.next
        return None
