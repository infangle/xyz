class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ch1 = defaultdict(int) #frequency count of haracters in s1
        ch2 = defaultdict(int) #frequency count of charactters in s2

        for c1 in s1:
            ch1[c1] += 1

        l = 0
        for r in range(len(s2)):
            ch2[s2[r]] += 1

            if r - l + 1 > len(s1):
                ch2[s2[l]] -= 1 #decrement frequency count
                if ch2[s2[l]] == 0: 
                    del ch2[s2[l]]
                l += 1

            if ch1 == ch2: #if same frequency count => permutation found
                return True

        return False

        