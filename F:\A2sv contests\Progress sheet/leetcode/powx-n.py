class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if x==0:
                return 0
            if n==0:
                return 1
            res = power(x, n//2)
            res *= res
            if n%2:
                return x*res
            else:
                return res

        res = power(x, abs(n))
        if n>=0:
            return res
        else:
            return 1/res
