import math
from collections import deque, Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    N, K = map(int, sys.stdin.readline().split())
    
    eliminated = N - K
    
    prize = eliminated * 10000
    print(prize)
    
solve()