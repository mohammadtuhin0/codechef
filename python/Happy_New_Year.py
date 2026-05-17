import math
from collections import deque, Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open('input.txt', 'w')
    sys.stdout = open('output.txt', 'r')
    
def solve():
    x = int(sys.stdin.readline())
    hours_left = 24 - x
    print(hours_left)

solve()