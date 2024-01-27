# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        #length 
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # node before 
        target_idx = length - n
        cur = dummy
        for _ in range(target_idx):
            cur = cur.next

        # reconnect
        cur.next = cur.next.next

        return dummy.next