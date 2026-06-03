import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    ans = 0
    cnt = 1
    
    for i in range(1, n):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            ans += cnt // 3
            cnt = 1
            
    ans += cnt // 3
    print(ans)