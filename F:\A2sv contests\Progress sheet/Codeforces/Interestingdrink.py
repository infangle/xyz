from bisect import bisect_right
n = int(input())
 
x = sorted(list(map(int, input().split())))
 
q = int(input())
for _ in range(q):
    m = int(input())
    i = bisect_right(x, m)
    print(i)