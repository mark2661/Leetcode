

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def create_node_list(root):
#     if root is None:
#         return []
#     return create_node_list(root.left) + [root] + create_node_list(root.right)
#
# def increaseing_order_ll(node_list):
#     for i in range(0,len(node_list) - 1):
#         node_list[i].left = None
#         node_list[i].right = node_list[i + 1]
#
#     node_list[-1].left = None
#     node_list[-1].right = None
#
#     return node_list[0]

# def increasing_order_ll(root):
#     if root is None:
#         return
#
#     if isLeaf(root):
#         return
#
#     increasing_order_ll(root.left)
#
#     if root.left:
#         root.left.right = root
#         root.left = None
#
#     increasing_order_ll(root.right)
#
# def isLeaf(root):
#     return root.left is None and root.right is None
#
# def find_left_most(root):
#     current = root
#     while current.left:
#         current = current.left
#     return current

class Solution:
    def increasingBST(self, root):
        smallest = find_left_most(root)
        increasing_order_ll(root)
        return smallest


# def print_answer(answer):
#     while answer.right:
#         print(answer.val)
#         answer = answer.right
#
# mySolution = Solution()
# tree = TreeNode(5,TreeNode(1),TreeNode(7))
# # answer = mySolution.increasingBST(tree)
# # print_answer(answer)
#
# for node in create_node_list(tree):
#     print(node.val)
