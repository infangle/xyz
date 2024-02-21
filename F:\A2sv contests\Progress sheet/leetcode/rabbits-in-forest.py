class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        
        ans = 0
        for key, val in count.items():
            grp = (key + val) // (key + 1)
            ans += (grp * (key + 1))


        return ans