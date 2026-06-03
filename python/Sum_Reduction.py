import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    seen = 0
    possible = True
    
    for x in arr:
        if seen & x:
            possible = False
            break
        seen |= x
        
    print("Yes" if possible else "No")