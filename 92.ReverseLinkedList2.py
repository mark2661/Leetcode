# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        if head is None or head.next is None:
            return head

        dummy = ListNode(0,head)
        current = dummy
        counter = 0


        while current and counter < left - 1:
            current = current.next
            counter += 1

        if current is None or current.next is None:
            return dummy.next

        lb = current
        lf = current.next
        c = lf.next
        l = lf

        while c and counter < right - 1:
            n = c.next
            c.next = l
            l = c
            c = n
            counter += 1

        lb.next = l
        lf.next = n

        return dummy.next

