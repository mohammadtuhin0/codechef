t = int(input())

for _ in range(t):
    n , k = map(int, input().split())
    
    remaining = n - k
    if remaining == 1:
        print("No")
    else:
        print("Yes")