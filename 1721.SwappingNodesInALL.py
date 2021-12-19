# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, k):
        if head is None or head.next is None:
            return head

        rear = back = front = head

        for _ in range(k-1):
            front = front.next
        rear = front
        front = front.next


        while front:
            front = front.next
            back = back.next

        rear.val, back.val = back.val, rear.val

        return head

