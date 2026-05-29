import math
from collections import Counter, deque, defaultdict
from bisect import bisect_right, bisect_left
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    
def solve():
    x = int(sys.stdin.readline())
    
    if x <= 60:
        print("YES")
    else:
        print("NO")
        
if __name__ == "__main__":
    solve()