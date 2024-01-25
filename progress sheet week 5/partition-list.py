# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head, right_head = None, None
        left_tail, right_tail = None, None

        while head:
            if head.val < x:
                if left_head is None:
                    left_head = head
                    left_tail = head
                else:
                    left_tail.next = head
                    left_tail = left_tail.next
            else:
                if right_head is None:
                    right_head = head
                    right_tail = head
                else:
                    right_tail.next = head
                    right_tail = right_tail.next
                
            head = head.next

        if left_tail:
            left_tail.next = right_head
        if right_tail:
            right_tail.next = None

        return left_head if left_head else right_head