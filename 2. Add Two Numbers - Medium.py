# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def reverse_ll(head):
#     previous = None
#     current = head
#     while current is not None:
#         temp = current.next
#         current.next = previous
#         previous = current
#         current = temp
#     return previous
#
# def create_value_from_ll(head):
#     current = head
#     val = ""
#     while current is not None:
#         val += str(current.val)
#         current = current.next
#     return val[-1::-1]
#
# def add_string_values(value_one, value_two):
#     return str(int(value_one) + int(value_two))[-1::-1]
#
# def generate_reverse_ll(value):
#     nodes = []
#     for num in value:
#         nodes.append(ListNode(int(num)))
#     for i in range(len(nodes) - 1):
#         nodes[i].next = nodes[i + 1]
#     return nodes[0]


class Solution:
    def addTwoNumbers(self, l1, l2):
        # result = add_string_values(create_value_from_ll(l1),create_value_from_ll(l2))
        # return generate_reverse_ll(result)

        p1 = l1
        p2 = l2
        dummy = ListNode()
        current = dummy
        carry = 0

        while (p1 is not None or p2 is not None):
            val1 = p1.val if p1 is not None else 0
            val2 = p2.val if p2 is not None else 0
            result = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            current.next = ListNode(result)
            current = current.next
            p1 = p1.next if p1 is not None else p1
            p2 = p2.next if p2 is not None else p2

        if carry != 0:
            current.next = ListNode(1)

        return dummy.next








# l1 = ListNode(2,ListNode(4,ListNode(3)))
# l2 = ListNode(5,ListNode(6,ListNode(4)))
# my_solution = Solution()
# my_solution.addTwoNumbers(l1,l2)