import math
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    R = int(sys.stdin.readline())
    
    if R <= 4:
        print("YES")
    else:
        print("NO")
        
if __name__ == "__main__":
    solve()