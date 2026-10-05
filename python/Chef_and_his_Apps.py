t = int(input())

for _ in range(t):
    s, x, y , z = map(int, input().split())
    free = s - (x + y)
    
    if free >= z:
        print(0)
    elif free + y >= z:
        print(1)
    else:
        print(2)