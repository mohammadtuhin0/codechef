import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = [int(x) for x in data[idx : idx + N]]
        idx += N
        
        # If the total sum is even, we can make all elements even.
        if sum(A) % 2 == 0:
            out.append("Yes")
        else:
            out.append("No")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()