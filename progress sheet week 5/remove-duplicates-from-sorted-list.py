# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = head
        cur = head.next
        visited = set()

        while cur:
            visited.add(prev.val)
            if cur.val in visited:
                next_node = prev.next
                prev.next = next_node.next
                del next_node
            else:
                prev = prev.next
            cur = cur.next
            

        return head
