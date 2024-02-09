class Solution:
    def numberOfWays(self, s: str) -> int:
        n0 = s.count("0")
        n1 = len(s) - n0

        prefix_sum_0 = [0] * (n0 + 1)
        prefix_sum_1 = [0] * (n1 + 1)

        c0, c1 = 0, 0

        res = 0

        for i, b in enumerate(s):
            if b == "0":
                c0 += 1
                prefix_sum_0[c0] = prefix_sum_0[c0 - 1] + 1
                res += prefix_sum_1[c1] * (n1 - prefix_sum_1[c1])
            else:
                c1 += 1
                prefix_sum_1[c1] = prefix_sum_1[c1 - 1] + 1
                res += prefix_sum_0[c0] * (n0 - prefix_sum_0[c0])
        
        return res