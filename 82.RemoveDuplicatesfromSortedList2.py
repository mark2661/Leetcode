# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):

        if head is None or head.next is None:
            return head

        dummy = ListNode(-101,head)
        back = dummy
        current = head
        front = dummy

        while front and current.next:
            front = current.next
            if front.val == current.val:
                while front.val == current.val:
                    front = front.next
                    if front is None:
                        break
                back.next = front
                current = front
            else:
                back = current
                current = current.next
        return dummy.next
