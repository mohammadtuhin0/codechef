# cook your dish here
import math
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys

if "LOCAL" in sys.argv:
    sys.stdin = open('input.txt', 'r')
    sys.stdin = open('output.txt', 'w')
    
def solve():
    x, y = map(int, sys.stdin.readline().strip().split())
    
    if x >= y:
        print("YES")
    else:
        print("NO")
        
if __name__ == "__main__":
    solve()
    
    
# python3 solution.py LOCAL
# sys.stdin.readline().strip()