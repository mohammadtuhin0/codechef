import math
from bisect import bisect_right, bisect_left
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    a, b = map(int, sys.stdin.readline().split())
    
    if a > b:
        print(a - b)
    else:
        print(0)
    
if __name__ == "__main__":
    solve()