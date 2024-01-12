class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_indx = {}
        match = inf

        for i, card in enumerate(cards):
            if card in last_indx:
                match = min(match, (i - last_indx[card] + 1))
            last_indx[card] = i

        if match == inf:
            return -1
        return match

        