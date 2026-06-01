import math
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from heapq import heappush, heappop, heapify
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    
def solve():
    N, k, R = map(int, sys.stdin.readline().split())
    left_pizza = N - k
    remaining_pizzas = left_pizza * R
    print(remaining_pizzas)
    
if __name__ == "__main__":
    solve()