import sys

def solve():
    # Read the number of test cases
    t = int(sys.stdin.readline())
    for _ in range(t):
        # Read A and B
        a, b = map(int, sys.stdin.readline().split())
        
        # Check if the sum is even
        if (a + b) % 2 == 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()