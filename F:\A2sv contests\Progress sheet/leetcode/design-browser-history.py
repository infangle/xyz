# using a doubly linkedlist
class ListNode:
    def __init__(self, x: str):
        self.val = x
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        # create a dummy node
        dummy = ListNode(homepage)
        self.size = 1 
        self.cur = dummy 
        print(self.cur.val)      

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.cur.next = node
        node.prev = self.cur
        self.size += 1
        self.cur = node

    def back(self, steps: int) -> str:
        if steps > self.size:
            steps = self.size - 1
        while steps and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)