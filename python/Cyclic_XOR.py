import sys
from math import gcd

MOD = 998244353

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    g = gcd(n, 1 << k)
    
    if (n // g) % 3 != 0:
        print(1)
    else:
        print(pow(2, 2 * g * k, MOD))