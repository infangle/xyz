class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        greater ={}

        days = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                top = stack.pop()
                greater[top] = i 
            stack.append(i)

        for i in range(len(temperatures)):
            if i in greater:
                days[i] = greater[i] - i
            else:
                days[i] = 0

        return days
