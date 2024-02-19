# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = {} #to store the address: value of each node visited
        a, b = headA, headB #two pointers at head of each linkedlist

        while a:
            if a not in nodes:
                nodes[a] = a.val
                a = a.next
            else:
                pre = a
                temp = a.next
                a.next = None
                pre.next = temp
                return a
        while b:
            if b not in nodes:
                nodes[b] = b.val
                b = b.next
            else:
                pre = b
                temp = b.next
                b.next = None
                pre.next = temp
                return b
        return None
                
                
                
                
            

