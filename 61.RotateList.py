# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def rotateRight(self, head, k):
    #     if head is None or k == 0:
    #         return head
    #     list_length = 1
    #     pointer = head
    #
    #     while pointer.next:
    #         pointer = pointer.next
    #         list_length += 1
    #
    #     pointer.next = head
    #     pointer = head
    #
    #     for i in range(1,list_length - (k % list_length)):
    #         pointer = pointer.next
    #
    #     temp = pointer.next
    #     pointer.next = None
    #     return temp
    def rotateRight(self, head, k):
        if head is None or k == 0:
            return head
        list_length = 1
        fast = head
        slow = head

        while fast.next:
            fast = fast.next
            list_length += 1


        fast = head

        for i in range(1,(k % list_length)):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = head
        temp = slow.next
        slow.next = None
        return temp
