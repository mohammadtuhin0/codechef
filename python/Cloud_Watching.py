import math
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    
def solve():
    a, b = map(int, sys.stdin.readline().split())
    
    if b >= a * 3:
        print("Rain")
    else:
        print("Dry")
        
if __name__ == "__main__":
    solve()