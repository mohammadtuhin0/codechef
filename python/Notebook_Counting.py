import math
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    a, b = map(int, sys.stdin.readline().split())
    
    page = b *2
    total_line = page * 50
    print(total_line * a)
    
if __name__ == "__main__":
    solve()