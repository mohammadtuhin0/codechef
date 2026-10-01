t = int(input())

for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    net_eport = (a1 - a2) + (b1 - b2)
    
    if net_eport < 0:
        print("YES")
    else:
        print("NO")