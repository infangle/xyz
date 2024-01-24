# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        dummy = ListNode(0)
        start = dummy

        while a and b:
            if a.val <= b.val:
                dummy.next = a
                a = a.next
            
            else:
                dummy.next = b
                b = b.next
            dummy = dummy.next  
        while a:
            dummy.next = a
            a = a.next
            dummy = dummy.next
        while b:
            dummy.next = b
            b = b.next
            dummy = dummy.next

        return start.next

        





        

        