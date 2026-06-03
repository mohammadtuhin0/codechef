import math
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    n = int(sys.stdin.readline())
    print(math.ceil((n + 1)/ 20))
    
if __name__ == "__main__":
    solve()