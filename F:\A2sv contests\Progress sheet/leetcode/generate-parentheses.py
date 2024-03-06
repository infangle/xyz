class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        comb = []
        def backtrack(open_c, close_c, comb):
            if open_c == close_c == n:
                res.append(''.join(comb[:]))
                return 
            if open_c < n:
                backtrack(open_c+1, close_c, comb + ['('])
            if close_c < open_c:
                backtrack(open_c, close_c+1, comb + [')'])
        backtrack(0,0, [])
        return res