import sys

if 'LOCAL' in sys.argv:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def solve():
    n = int(sys.stdin.readline())

    day = n * 3
    print(day)
    
solve()