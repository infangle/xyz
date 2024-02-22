class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ch = {} #to store the character and its last appeared index
        for i, c in enumerate(s):
            last_ch[c] = i

        ans = []
        part_len, last = 0, 0
        for i in range(len(s)):
            part_len += 1
            last = max(last, last_ch[s[i]])

            if i == last:
                ans.append(part_len)
                part_len = 0

        return ans

            


        