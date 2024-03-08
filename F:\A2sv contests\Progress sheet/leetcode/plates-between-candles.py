from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        prefix_sum = [0] * n
        left_c = [-1] * n #right occurance
        right_c = [-1] * n #left occurance

        for i in range(n):
            prefix_sum[i] = prefix_sum[i-1] + (1 if s[i] == '*' else 0)
            left_c[i] = i if s[i] == '|' else left_c[i-1]

        right_c[-1] = n - 1 if s[-1] == '|' else n
        for i in range(n-2, -1, -1):
            right_c[i] = i if s[i] == '|' else right_c[i+1]

        res = []
        for query in queries:
            start, end = query
            start = right_c[start]
            end = left_c[end]
            if start >= end:
                res.append(0)
            else:
                res.append(prefix_sum[end] - prefix_sum[start])

        return res
