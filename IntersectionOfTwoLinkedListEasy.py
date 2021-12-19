


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def getIntersectionNode(self, headA, headB):
#         my_dict = dict()
#
#         current = headA
#         while current != None:
#             my_dict[(current)] = current
#             current = current.next
#
#         current = headB
#         while current != None:
#             if my_dict.get(current) != None:
#                 return my_dict[(current)]
#             current = current.next
#         return None

class Solution: # O(n) time, O(1) space solution. Only works if all values in both LL are positive.
    def getIntersectionNode(self, headA, headB):

        current = headA
        while current != None:
            current.val = -1 * current.val
            current = current.next

        current = headB
        intersectionNode = None
        while current != None:
            if current.val < 0:
                intersectionNode = current
                break
            current = current.next

        current = headA
        while current != None:
            current.val = -1 * current.val
            current = current.next

        return intersectionNode