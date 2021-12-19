# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        lst = []
        def convertLLTOArray(head):
            current = head
            while current:
                lst.append(current.val)
                current = current.next
            return lst

        def ArrayToBST(start, end):
            if end < start:
                return None
            mid = (start + end) // 2
            new_root = TreeNode(lst[mid])
            new_root.left = ArrayToBST(start, mid - 1)
            new_root.right = ArrayToBST(mid + 1, end)
            return new_root

        return ArrayToBST(0,len(convertLLTOArray(head)) - 1)
