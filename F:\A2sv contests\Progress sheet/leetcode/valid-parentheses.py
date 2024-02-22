class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '{':'}', '[':']'}
        r = []
        for b in s:
            if b in valid:
                r.append(b)
            elif b in valid.values():
                if not r:
                    return False
                else:
                    if valid[r.pop()] != b:
                        return False
        if len(r) == 0:
            return True 
            
            