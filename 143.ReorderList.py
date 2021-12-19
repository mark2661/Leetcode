# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        if head is None or head.next is None:
            return head
        self.stack = []

        #Find centre
        dummy = ListNode(0,head)
        slow = dummy
        runner = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            runner = runner.next
        if fast:
            slow = runner
            runner = runner.next

        #remove links
        while runner:
            self.stack.append(runner)
            slow.next = None
            slow = runner
            runner = runner.next

        #swap links
        back = head
        front = head.next
        while len(self.stack) > 0:
            mid = self.stack.pop()
            back.next = mid
            mid.next = front
            back = front
            front = front.next if front else None

        return head
