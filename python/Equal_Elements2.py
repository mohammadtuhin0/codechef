from collections import Counter
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        # Extract the slice of the array for the current test case
        a = data[idx : idx + n]
        idx += n
        
        # Count frequencies using Counter
        freq = Counter(a)
        
        # The most common element's frequency
        max_freq = freq.most_common(1)[0][1]
        
        # Minimum operations = Total elements - Max frequency
        out.append(str(n - max_freq))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()