import math
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    x, y = map(int, sys.stdin.readline().split())
    
    food_cost = x * 6
    total_cost = food_cost + y
    print(total_cost)
    
if __name__ == "__main__":
    solve()