def solve(A, B, P, Q, R):
    ans = float('inf')
    
    for k in range(min(A, B) + 1):
        cost = k * R
        cost += ((A - k + 1) // 2) * P
        cost += ((B - k + 1) // 2) * Q
        
        ans = min(ans, cost)
        
    return ans

t = int(input())
for _ in range(t):
    A, B, P, Q, R = list(map(int, input().split()))
    
    print(solve(A, B, P, Q, R))