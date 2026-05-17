import math
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open('input.txt', 'w')
    sys.stdout = open('output.txt', 'r')
    
def solve():
    x, y = map(int, sys.stdin.readline().split())
    if x <= y:
        print("YES")
    else:
        print("NO")
        
solve()