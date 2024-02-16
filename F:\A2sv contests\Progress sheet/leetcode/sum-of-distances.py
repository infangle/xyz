class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        if len(set(nums)) == len(nums): 
            return [0]*len(nums)
        
        idx = {}  

        for i, num in enumerate(nums):
            if num not in idx:
                idx[num] = []
            idx[num].append(i)

        
        ans = [0]*len(nums)
        for num, val in idx.items():
            suffix_sum = sum(val)
            prefixSum = 0
            s = len(val)
            p = 0
            for i in val:
                prefixSum += i
                p += 1
                suffix_sum -= i
                s -= 1
                ans[i] = (p*i - prefixSum) + (suffix_sum - s*i)

        return ans