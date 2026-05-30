import math
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    X, H = map(int, sys.stdin.readline().split())
    
    total_hours = 24 * (X - 4) + H
    print(total_hours)
    
if __name__ == "__main__":
    solve()