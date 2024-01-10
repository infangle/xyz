class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_dict = defaultdict(int)
        p_dict = defaultdict(int)
        k = len(p)

        # counting charcters in p
        for char in p:
            p_dict[char] += 1
           
        
        # initializing pointers and s dictionary
        l = 0
        r = k
        for ch in s[:k]:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1

        #anagram list

        anagram = []

        if p_dict == s_dict:
            anagram.append(0)

        while r < len(s):
            # shifting the left pointer
            s_dict[s[l]] -= 1
            if s_dict[s[l]] == 0:
                del s_dict[s[l]]
            l += 1
            
            # adding the right

            s_dict[s[r]] += 1

             # if anagram found
            if p_dict == s_dict:
                anagram.append(l)

            r += 1
            
        


        return anagram

            


        


        