class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s)+1)
        string = list(s)

        for l, r, c in shifts:
            if c == 1:
                prefix[l] += 1
                prefix[r + 1] -= 1
            elif c == 0:
                prefix[l] -= 1
                prefix[r+1] += 1
            
        for i in range(1,len(prefix)):
            prefix[i] = prefix[i-1] + prefix[i]
        
        for i in range(len(s)):
            string[i] = chr(((ord(s[i]) - ord('a')) +prefix[i]) % 26 + ord('a')) 

        return ''.join(string)
