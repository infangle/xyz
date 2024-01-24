# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        visited = set()
        visited.add(cur)

        while cur and  cur.next:
            cur = cur.next
            if cur not in visited:
                visited.add(cur)
            else:
                return True
        return False
                