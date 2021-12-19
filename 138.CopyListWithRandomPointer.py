
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        dummy = Node(0)
        co = head
        cc = dummy
        ht = dict()

        while co:
            newNode = ht[co] if co in ht else Node(co.val)
            newRandom = None
            ht[co] = newNode
            if co.random:
                newRandom = ht[co.random] if co.random in ht else Node(co.random.val)
                if co.random not in ht:
                    ht[co.random] = newRandom

            newNode.random = newRandom

            cc.next = newNode
            co = co.next
            cc = cc.next

        return dummy.next

