# Read the number of test cases
t = int(input())

for _ in range(t):
    n = int(input())
    # A pizza can be cut into 1 piece (0 cuts) or any even number of pieces
    if n == 1 or n % 2 == 0:
        print("YES")
    else:
        print("NO")