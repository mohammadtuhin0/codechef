import math
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    
def solve():
    n = int(sys.stdin.readline())
    
    if n % 2== 0:
        print(1)
    else:
        print(2)
    
if __name__ == "__main__":
    solve()