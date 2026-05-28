import math
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    
def solve():
    A, B, C = map(int, sys.stdin.readline().split())
    
    if A * B == C * C:
        print("Yes")
    else:
        print("No")
        
solve()