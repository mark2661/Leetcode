# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def sortList(self, head):
#         if head is None or head.next is None:
#             return head
#         runner = back = head
#         front = head.next
#         swapped = True
#         gap = 1
#         while swapped:
#             for _ in range(gap):
#                 if runner:
#                     runner = runner.next
#                 else:
#                     return head
#             swapped = False
#             while runner:
#                 if back.val > front.val:
#                     back.val, front.val = front.val, back.val
#                     swapped = True
#                 front = front.next
#                 back = back.next
#                 runner = runner.next
#             gap += 1
#             runner = head
#             back = head
#             front = head.next
#         return head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        mid = self.findMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def findMid(self, head):
        if not head.next.next:
            temp = head.next
            head.next = None
            return temp
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp

    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if right.val < left.val:
                current.next = right
                current = right
                right = right.next
            else:
                current.next = left
                current = left
                left = left.next
        if right:
            current.next = right
        if left:
            current.next = left
        return dummy.next


