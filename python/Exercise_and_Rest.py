import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open('input.txt', 'w')
    sys.stdout = open('output.txt', 'r')

def solve():
    n = int(sys.stdin.readline())

    day = n * 3
    print(day)
    
solve()