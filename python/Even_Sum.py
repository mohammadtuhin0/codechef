import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    total = sum(arr)
    
    if total % 2 == 0:
        if any(x % 2 == 0 for x in arr):
            print("Yes")
        else:
            print("No")
    else:
        if any(x % 2 == 1 for x in arr):
            print("Yes")
        else:
            print("No")
        