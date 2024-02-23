class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        cards = deque()

        deck = sorted(deck, reverse=True)

        for i in range(len(deck)):
            if cards:
                cards.appendleft(cards.pop())
            cards.appendleft(deck[i])

        return cards