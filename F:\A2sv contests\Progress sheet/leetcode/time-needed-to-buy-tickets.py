from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for i in range(len(tickets)):
            queue.append(i)

        t = 0

        while queue:
            enq = queue.popleft()
            tickets[enq] -= 1

            if tickets[enq]>=1:
                queue.append(enq)

            t += 1

            if tickets[k] == 0:
                return t




        