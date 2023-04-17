# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        l1 = []

        while head:
            l1.append(head.val)
            head = head.next

        if len(l1) == 0:
            return None

        l1 = l1[::-1]
        n = ListNode()
        header = ListNode()

        for i in range(len(l1)):
            if i == 0:
                n.val = l1[i]
                header = n
            else:
                cur = ListNode()
                cur.val = l1[i]
                n.next = cur
                n = n.next

        return header








