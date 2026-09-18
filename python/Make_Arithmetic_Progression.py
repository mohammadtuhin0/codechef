t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    if y - x == z - y:
        print(0)
    else:
        print(1)