t = int(input())

for _ in range(t):
    # Read N, X, Y
    n, x, y = map(int, input().split())
    
    # Calculate total space needed
    total_needed = x + (2 * y)
    
    # Compare with available space N
    if n >= total_needed:
        print("YES")
    else:
        print("NO")