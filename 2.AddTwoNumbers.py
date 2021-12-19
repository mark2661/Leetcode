# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        def getVal(head):
            if not head:
                return 0
            current = head
            val = 0
            counter = 0
            while current:
                val =  val + (current.val * pow(10,counter))
                counter += 1
                current = current.next
            return val
        val1 = getVal(l1)
        val2 = getVal(l2)
        result = val1 + val2
        if result == 0:
            return ListNode()
        dummy = ListNode()
        current = dummy
        while result > 0:
            v = result % 10
            result = result // 10
            current.next = ListNode(v)
            current = current.next
        return dummy.next
