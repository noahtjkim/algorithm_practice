
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = ListNode()

        while True:
            print(list1.val)

            if list1.next == None:
                break


        return arr


sol = Solution()
res = sol.mergeTwoLists([1, 2, 4], [1, 3, 4])
# print(res)



