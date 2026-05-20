import math
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    A, B, C = map(int, sys.stdin.readline().split())
    
    if A * B == C * C:
        print("Yes")
    else:
        print("No")
        
solve()