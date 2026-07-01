# Read the three space-separated integers
x, n, m = map(int, input().split())

# Check if the total amount (x + m) is sufficient to cover the price (n)
if x + m >= n:
    print("YES")
else:
    print("NO")