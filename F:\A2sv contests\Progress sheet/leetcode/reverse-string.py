class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverser (l:int, r:int, w: List[str]):
            if l >= r:
                return 

            w[l], w[r] = w[r], w[l]

            reverser(l+1, r-1, w)
        l, r = 0, len(s) - 1
        w = s
        reverser(l, r, w)