import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    idx = 1
    for _ in range(T):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        
        # k is the number of multiples of x in the range [x, y]
        k = y // x
        
        # If x is even, all multiples are even -> YES
        # If x is odd, the answer depends on whether k is even or odd
        if x % 2 == 0 or k % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()