class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        idx = {}
        starts = []
        ends = []
        s_e = {}
        for i, interval in enumerate(intervals):
            idx[interval[0]] = i
            starts.append(interval[0])
            ends.append(interval[1])
            s_e[interval[0]] = interval[1]
        starts.sort()
        
        ans = [-1]*len(intervals)
        for i in range(len(ends)):
            r_idx = bisect_left(starts, ends[i])
            if r_idx < len(starts):
                s = starts[r_idx]
                ans[i] = idx[s]
            else:
                continue
        return ans