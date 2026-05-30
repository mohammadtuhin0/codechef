import math
from collections import Counter, deque, defaultdict
from bisect import bisect_right, bisect_left
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    
def solve():
    N, A, B = map(int, sys.stdin.readline().split())
    
    spend = A * B
    still_has = N - spend
    print(still_has)
    
if __name__ == "__main__":
    solve()