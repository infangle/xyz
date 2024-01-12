class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k > len(blocks):
            return -1

        count = 0 # count of white blocks 
        l = 0 
        r = 0 
        ans = float("inf") 

        
        while r < len(blocks): 

            if blocks[r] == 'W': 
                count += 1 

            while l <= r and r - l + 1 >= k: 

                if r - l + 1 == k: # if the window is valid
                    ans = min(ans, count) # update 
                
                 #shrink
                if blocks[l] == 'W':
                    count -= 1 
                l += 1 
            r += 1 

        if ans == float("inf"): 
            return -1 
        else:
            return ans 
