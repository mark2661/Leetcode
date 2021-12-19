# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if head.next is None:
            return None
        dummy = ListNode(0,head)
        bp = dummy
        lp = dummy
        delHead = False

        for i in range(n + 1):
            lp = lp.next
            # if lp:
            #     lp = lp.next
            # else:
            #     delHead = True

        while lp is not None:
            lp = lp.next
            bp = bp.next

        # if delHead:
        #     return bp.next

        temp = bp.next
        bp.next = bp.next.next
        temp.next = None

        return dummy.next

