from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        ban_cnt = {'D': 0, 'R': 0}

        queue = deque(list(senate))

        while queue and count['D'] and count['R']:
            if ban_cnt[queue[0]] == 0:
                s = queue.popleft()
                queue.append(s)
                if s == 'D':
                    ban_cnt['R'] += 1
                    count['R'] -= 1
                else:
                    ban_cnt['D'] += 1
                    count['D'] -= 1 
            else:
                while ban_cnt[queue[0]]:
                    p = queue.popleft()
                    ban_cnt[p] -= 1

        if count['D']:
            return 'Dire'
        return 'Radiant'

