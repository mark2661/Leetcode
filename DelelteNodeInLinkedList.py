# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

# def delNode(node):
#     new_val = None
#     if node.next != None:
#         new_val = delNode(node.next)
#
#     current_value = node.val
#     node.val = new_val if new_val != None else node.val
#     return current_value
#
#
# class Solution:
#     def deleteNode(self, node):
#         delNode(node)
#         current = node
#         while(current.next.next != None):
#             current = current.next
#         current.next = None
#
#
# input = ListNode(5,ListNode(1,ListNode(9)))
# Solution(input)


class Solution:
    def deleteNode(self, node):
     new_next = node.next.next
     new_val = node.next.val

     node_to_delete = node.next

     node.val = new_val
     node.next = new_next

     node_to_delete.next = None
     node_to_delete = None
