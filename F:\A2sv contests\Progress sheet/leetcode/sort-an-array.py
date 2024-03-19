class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half, right_half):
            ans = []
            l, r = 0, 0

            while l < len(left_half) and r < len(right_half):
                if left_half[l] < right_half[r]:
                    ans.append(left_half[l])
                    l += 1
                else:
                    ans.append(right_half[r])
                    r += 1 
            ans.extend(left_half[l:])
            ans.extend(right_half[r:])

            return ans

        def mergesort(left, right, arr):
            if left == right:
                return [arr[left]]
            
            mid = (left + right) // 2

            left_half = mergesort(left, mid, arr)
            right_half = mergesort(mid + 1, right, arr)

            return merge(left_half, right_half)

        return mergesort(0, len(nums) - 1, nums)
        