import math
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    x, y = map(int, sys.stdin.readline().split())
    
    small_room = x * 30
    large_room = y * 60
    
    total_time = small_room + large_room
    print(total_time)
    
if __name__ == "__main__":
    solve()