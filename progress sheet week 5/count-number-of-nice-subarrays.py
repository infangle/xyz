class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        def count_nice(nums, k):
            l = 0
            odds = 0
            nice = 0

            #for
            for r in range(len(nums)): 
                odds += nums[r]
            
                # while
                while odds > k:
                    odds -= nums[l] # then subtract nums[l]
                    l += 1

                # update
                nice += (r-l+1)
                

            return nice
        return count_nice(nums,k)-count_nice(nums,k-1)


