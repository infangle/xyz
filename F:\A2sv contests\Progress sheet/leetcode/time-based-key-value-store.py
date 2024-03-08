class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append(value)
        self.time[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        target = self.time[key]
        ans = self.vals[key]
        t = bisect_right(target, timestamp)
        if t == 0:
            return ""
        else:
            return ans[t-1]
            

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)