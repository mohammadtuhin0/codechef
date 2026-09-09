t = int(input())

for _ in range(t):
    n = int(input())
    a = str(input())
    b = str(input())
    
    if a.count('a') == b.count('b'):
        print("YES")
    else:
        print("NO")