# cook your dish here
import math
import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open('input.txt', 'w')
    sys.stdout = open('output.txt', 'r')
    

def solve():
    X, Y, H = map(int, sys.stdin.readline().split())
    extra = (H - 1)
    
    pay = X + (extra * Y)
    
    print(pay)

solve()