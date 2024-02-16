t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()  
    prefix_sum = [0] * (n + 1)
    sum_dist = {0: 1}  
    ans = 0

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + int(a[i])
        
        p_i_minus_i = prefix_sum[i + 1] - (i + 1)
        
        if p_i_minus_i in sum_dist:
            ans += sum_dist[p_i_minus_i]
            
        sum_dist[p_i_minus_i] = sum_dist.get(p_i_minus_i, 0) + 1

    print(ans)
