n = int(input())

x = [int(x) for x in input().split()]

v=[int(x) for x in input().split()]

def rightmost_left_ep(t):
    return max([x[i]-(v[i]*t) for i in range(n)])

def leftmost_right_ep(t):
    return min([x[i]+(v[i]*t) for i in range(n)])

def is_feasible(K):
    return rightmost_left_ep(K) <= leftmost_right_ep(K)

L,R = 0.0, 1e9

while abs(R-L)>1e-6:
    mid=(L+R)/2
    
    if(is_feasible(mid)): 
        R=mid
    
    else: 
        L=mid
        
print(mid)