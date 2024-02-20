class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks, key=lambda x: x[0] - x[1])
        print(tasks)
        ans = 0
        e = 0
        for a, m in tasks:
            if e <= m:
                ans += m - e
                e = m 
            e -= a

        return ans