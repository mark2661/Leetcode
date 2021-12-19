# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0,head)
        back = dummy
        middle = head
        front = head.next

        while front:
            back.next = front
            middle.next = front.next
            front.next = middle

            back = middle
            if middle.next:
                front = middle.next.next
            else:
                front = middle.next
            middle = middle.next

        return dummy.next




