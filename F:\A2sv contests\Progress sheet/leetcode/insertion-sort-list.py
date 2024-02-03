# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)  # Create a dummy node
        dummy.next = head
        curr = head

        while curr and curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next  # No need to move the current node
            else:
                temp = curr.next  # Store the node to be inserted
                curr.next = curr.next.next  # Remove the node to be inserted from the list

                # Find the correct position to insert the node
                prev = dummy
                while prev.next and prev.next.val < temp.val:
                    prev = prev.next

                # Insert the node at the correct position
                temp.next = prev.next
                prev.next = temp

        return dummy.next