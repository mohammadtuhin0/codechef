import sys

MOD = 998244353
MAXN = 200005

fact = [1] * MAXN
for i in range(1, MAXN):
    fact[i] = fact[i - 1] * i % MOD

invfact = [1] * MAXN
invfact[MAXN - 1] = pow(fact[MAXN - 1], MOD - 2, MOD)

for i in range(MAXN - 2, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD


def C(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD


t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    ans = 0

    for x in range(1, n + 1):
        ways_choose_tail = C(n - x, n - k)
        ways_prefix = pow(x - 1, k - 1, MOD)

        ans = (ans + ways_choose_tail * ways_prefix) % MOD

    print(ans)