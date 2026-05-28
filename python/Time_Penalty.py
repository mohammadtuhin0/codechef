import math
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    
def solve():
    x, y = map(int, sys.stdin.readline().split())
    penalty = x + y * 10
    print(penalty)
    
if __name__ == "__main__":
    solve()