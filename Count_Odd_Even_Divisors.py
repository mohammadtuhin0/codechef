import sys

def solve():
    n = int(sys.stdin.readline())
    odd = 0
    even = 0
    
    # Iterate from 1 to N to find all divisors
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
                
    print(odd, even)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
