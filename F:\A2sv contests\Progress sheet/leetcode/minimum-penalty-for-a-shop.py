class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_count_N = [0] * (n + 1)
        suffix_count_Y = [0] * (n + 1)
        
        for i in range(n):
            prefix_count_N[i + 1] = prefix_count_N[i] + (customers[i] == 'N')
        
        for i in range(n - 1, -1, -1):
            suffix_count_Y[i] = suffix_count_Y[i + 1] + (customers[i] == 'Y')
        
        min_penalty = float('inf')
        best_hour = -1
        
        for i in range(n + 1):
            penalty = prefix_count_N[i] + suffix_count_Y[i]
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i
        
        return best_hour