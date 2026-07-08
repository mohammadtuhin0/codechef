T = int(input())

for _ in range(T):
    R, Y = map(int, input().split())
    ans = R + max(0, (Y-R) // 2)
    print(ans)