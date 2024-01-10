class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)

        for c in s1:
            s1_dict[c] += 1

        l = 0
        
        
        # for
        for r in range(len(s2)):
            s2_dict[s2[r]] += 1
            
            # while
            while r-l+1 > k:
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l += 1

            # update 
            if s1_dict == s2_dict:
                return True
           
        return False

            