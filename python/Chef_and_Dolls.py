import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    ans = 0
    for _ in range(N):
        doll = int(input())
        ans ^= doll

    print(ans)