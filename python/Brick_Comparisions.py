T = int(input())


for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    
    for i in range(1, N):
        if(A[i] > A[ans]):
            ans = i
        
    print(ans + 1)