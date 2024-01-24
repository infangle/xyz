# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        bef = None

        while slow:
            nxt = slow.next
            slow.next = bef
            bef = slow
            slow = nxt
        
        while head and bef:
            if head.val != bef.val:
                return False
            bef = bef.next
            head = head.next
        return True


        