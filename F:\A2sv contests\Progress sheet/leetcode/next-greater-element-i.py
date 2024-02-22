class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonic queue(strictly increasing)
        stack = []
        next_greater = [-1] * len(nums1)
        greater = {} 
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                top = stack.pop()
                greater[top] = nums2[i]
            stack.append(nums2[i])
        
        for i in range(len(nums1)):
            if nums1[i] in greater:
                next_greater[i] = greater[nums1[i]]
            else:
                next_greater[i] = -1


        return next_greater


        