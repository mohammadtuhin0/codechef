import math 
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    
def solve():
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a + b > c and b + c > a and a + c > b:
        print("YES")
    else:
        print("NO")
        
if __name__ == "__main__":
    solve()