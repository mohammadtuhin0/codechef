import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    results = []
    for _ in range(T):
        W = int(data[idx])
        P = int(data[idx+1])
        K = int(data[idx+2])
        idx += 3
        
        if K <= W:
            results.append(str(2 * K))
        else:
            results.append(str(W + K))
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()