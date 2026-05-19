import math
from collections import deque, Counter, defaultdict
from bisect import bisect_right, bisect_left
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", 'w')
    sys.stdout = open("output.txt", "r")
    
def solve():
    L, R = map(int, sys.stdin.readline().split())
    if L > R:
        print(L - R)
    elif L < R:
        print(R - L)
    else:
        print(0)
    
solve()