class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return []
        # prefix product 
        prefixProd = [0] * len(nums)
        prefixProd[0] = 1

        for i in range(1, len(nums)):
            prefixProd[i] = prefixProd[i - 1] * nums[i - 1]

        #suffix product 
        suffixProd = [0] * len(nums)
        suffixProd[-1] = 1
        
        for i in range(len(nums) - 2, -1, -1):
            suffixProd[i] = suffixProd[i + 1] * nums[i + 1]
        
        ans = []
        
        for i in range(len(nums)):
            ans.append(prefixProd[i] * suffixProd[i])
        
        return ans
