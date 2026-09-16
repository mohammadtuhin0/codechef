a, b = map(int, input().split())

diff = a - b
if diff % 2 == 0:
    print(int((a - b ) / 2))
else:
    print(-1)