
#Definition for singly-linked list.

# def populate_list(new_list,old_list):
#
#     current = old_list
#     while current != None:
#         new_list.append(current.val)
#         current = current.next
#     return new_list
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#
#         pointer_one = l1
#         pointer_two = l2
#         new_list = []
#
#         if pointer_one.val == pointer_two.val:
#             new_list.append(pointer_one.val)
#             new_list.append(pointer_two.val)
#             pointer_one = pointer_one.next
#             pointer_two = pointer_two.next
#
#         elif pointer_one.val > pointer_two.val:
#             new_list.append(pointer_two.val)
#             pointer_two = pointer_two.next
#
#         else:
#             new_list.append(pointer_one.val)
#             pointer_one = pointer_one.next
#
#         while (pointer_one != None and pointer_two != None):
#
#             if pointer_one.val == pointer_two.val:
#                 new_list.append(pointer_one.val)
#                 new_list.append(pointer_two.val)
#                 pointer_one = pointer_one.next
#                 pointer_two = pointer_two.next
#
#             elif pointer_one.val > pointer_two.val:
#                 new_list.append(pointer_two.val)
#                 pointer_two = pointer_two.next
#
#             else:
#                 new_list.append(pointer_one.val)
#                 pointer_one = pointer_one.next
#
#         return populate_list(new_list, pointer_one if pointer_one == None else pointer_two)


# my_solution = Solution()
# print(my_solution.mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))),ListNode(1,ListNode(3,ListNode(4)))))


#Definition for singly-linked list.

def populate_list(new_list, old_list):

    while old_list != None:
        new_list.next = old_list
        new_list = new_list.next
        old_list = old_list.next
    return new_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):

        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1

        pointer_one = l1
        pointer_two = l2

        if pointer_one.val == pointer_two.val:
            new_list = ListNode(pointer_one.val)
            head = new_list
            new_list.next = pointer_two
            new_list = new_list.next
            pointer_one = pointer_one.next
            pointer_two = pointer_two.next

        elif pointer_one.val > pointer_two.val:
            new_list = ListNode(pointer_two.val)
            head = new_list
            #new_list = new_list.next
            pointer_two = pointer_two.next

        else:
            new_list = ListNode(pointer_one.val)
            head = new_list
            #new_list = new_list.next
            pointer_one = pointer_one.next

        if pointer_one == None and pointer_two!= None:
            populate_list(new_list,pointer_two)

        elif pointer_two == None and pointer_one != None:
            populate_list(new_list,pointer_one)

        while (pointer_one != None and pointer_two != None):

            if pointer_one.val == pointer_two.val:
                new_list.next = pointer_one
                new_list = new_list.next
                new_list.next = pointer_two
                new_list = new_list.next
                pointer_one = pointer_one.next
                pointer_two = pointer_two.next

            elif pointer_one.val > pointer_two.val:
                new_list.next = pointer_two
                new_list = new_list.next
                pointer_two = pointer_two.next

            else:
                new_list.next = pointer_one
                new_list = new_list.next
                pointer_one = pointer_one.next

        old_list = pointer_one if pointer_one == None else pointer_two

        while old_list != None:
            new_list.next = old_list
            new_list = new_list.next
            old_list = old_list.next

        return head

my_solution = Solution()
# print(my_solution.mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))),ListNode(1,ListNode(3,ListNode(4)))))
#print(my_solution.mergeTwoLists(ListNode(2),ListNode(1)))
print(my_solution.mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))),ListNode(5)))