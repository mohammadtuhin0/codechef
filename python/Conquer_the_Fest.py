import math
from collections import deque, Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    N, B = map(int, sys.stdin.readline().split())
    
    if N >= B * 10:
        print("YES")
    else:
        print("NO")
        
solve()