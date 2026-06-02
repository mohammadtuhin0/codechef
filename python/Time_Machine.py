import math
from bisect import bisect_right, bisect_left
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    a = int(sys.stdin.readline())
    if a + 25 >= 2050:
        print("YES")
    else:
        print("NO")
        
if __name__ == "__main__":
    solve()