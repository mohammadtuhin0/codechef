# cook your dish here

import math
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open('input.txt', 'w')
    sys.stdout = open('output.txt', 'r')

def solve():
    R, C, E = map(int, sys.stdin.readline().split())
    m = (R + E) * C
    print(m)
    
solve()