class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = {} # count the frequency of each character in t
        s_counter = {} # count the frequency of each character in s that is in t
        windows = {} # store the start and end index of each valid window with its length
        required = 0 # the number of unique characters in t
        formed = 0 # the number of unique characters in s that match the frequency in t

        if t == "": # if t is empty, return empty string
            return ""

        for char in t: # initialize the counters
            if char in t_counter:
                t_counter[char] += 1
            else:
                t_counter[char] = 1
                required += 1
            s_counter[char] = 0

        l = 0 # start index of the window
        r = 0 # end index of the window

        while r < len(s): # loop through s
            if s[r] in s_counter: # if the current character is in t
                s_counter[s[r]] += 1 # increment the counter
                if s_counter[s[r]] == t_counter[s[r]]: # if the frequency matches
                    formed += 1 # increment the formed count
            while l <= r and formed == required: # if the window is valid
                windows[(l,r)] = r - l + 1 # store the window and its length
                if s[l] in s_counter: # if the leftmost character is in t
                    s_counter[s[l]] -= 1 # decrement the counter
                    if s_counter[s[l]] < t_counter[s[l]]: # if the frequency drops
                        formed -= 1 # decrement the formed count
                l += 1 # move the left pointer
            r += 1 # move the right pointer

        ans = "" # the answer string
        mini = float("inf") # the minimum length
        for key, val in windows.items(): # loop through the windows
            if val < mini: # if the length is smaller
                mini = val # update the minimum length
                ans = s[key[0]:key[1]+1] # update the answer string

        return ans # return the answer
