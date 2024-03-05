class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(i, before):
            if len(s) == i:
                return True
            for j in range(i, len(s)):
                nxt = int(s[i:j+1])
                if nxt + 1 == before and backtrack(j+1, nxt):
                    return True
            return False

        for i in range(len(s)-1):
            val = int(s[:i+1])
            if backtrack(i+1, val):
                return True
        return False
