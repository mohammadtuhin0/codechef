# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read X and Y from the input
    x, y = map(int, input().split())
    
    # Check if Y is in the range [X, X + 200]
    if x <= y <= x + 200:
        print("YES")
    else:
        print("NO")