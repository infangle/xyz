# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = head, head

        dummyR = ListNode()
        dummyL = ListNode()
        less = dummyL
        greater = dummyR

        while right and left:
            if right.val < x:
                dummyL.next = right 
                dummyL = dummyL.next
            else:
                dummyR.next = right
                dummyR = dummyR.next
            right = right.next
        dummyR.next = None
        dummyL.next = greater.next
        return less.next



                
                