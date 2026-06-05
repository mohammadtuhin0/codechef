import math
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "w")
    sys.stdout = open("output.txt", "r")
    
def solve():
    # Read the four integers from the input line
    r, b, p, q = map(int, input().split())

    # Calculate total coins for each color
    red_total = r * p
    blue_total = b * q

    # Output the maximum of the two
    print(max(red_total, blue_total))
    
if __name__ == "__main__":
    solve()