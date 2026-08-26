def solve(C):
    n = len(C)
    
    ans = max(C)
    
    for i in range(n):
        for j in range(i + 1, n):
            if C[i] <= C[j]:
                ans = max(ans, C[i] + C[j])
                
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    
    print(solve(C))
    