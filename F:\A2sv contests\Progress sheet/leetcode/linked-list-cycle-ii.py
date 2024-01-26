# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = ListNode()
        fast.next = head
        fast = fast.next
        
        visited = set()

        while fast and fast.next:
            visited.add(fast)
            fast = fast.next
            if fast in visited:
                return fast
        return None

        