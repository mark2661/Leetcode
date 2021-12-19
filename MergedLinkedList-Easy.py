class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):

        if l1 == None and l2 == None:
            return None

        if l1 != None and l2 == None:
            return l1

        if l1 == None and l2 != None:
            return l2

        root = ListNode()
        current = root

        stop = False

        while not stop:
            if l1.val < l2.val:
                current.next = l1
                current = current.next
                l1 = l1.next

            else:
                current.next = l2
                current = current.next
                l2 = l2.next

            if l1 == None:
                current.next = l2
                stop = True

            elif l2 == None:
                current.next = l1
                stop = True
                
        return root.next


my_solution = Solution()
# l1 = ListNode(1,ListNode(2,ListNode(4)))
# l2 = ListNode(1,ListNode(3,ListNode(4)))
l1 = ListNode(5)
l2 = ListNode(1,ListNode(2,ListNode(4)))
root = my_solution.mergeTwoLists(l1,l2)
current = root

while current != None:
    print(current.val)
    current = current.next
