# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # defining the length of the original linkedlist
        i = 0 #number of nodes
        cur = head
        while cur:
            i += 1
            cur = cur.next
        if i == 0:
            return [None]* k

        lengths = [] #len of each part
        
        # based on the hint
        for j in range(k):
            p = i//k #number of nodes for every part
            if j < i%k:
                p += 1
            lengths.append(p)
        
        
        ans = [] #list of head nodes for each part
        cur = head
        nxt = head.next
        for l in lengths:
            while l > 1 and cur and cur.next :
                cur = cur.next
                nxt = nxt.next
                l -= 1
            cur.next = None
            ans.append(head)
            head = nxt
            
            if nxt: 
                cur = head
                nxt = nxt.next
                
                
               
        return ans
            
        
            
            
            