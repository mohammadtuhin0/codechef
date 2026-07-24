# Read the number of test cases
for _ in range(int(input())):
    # Read W, X, Y, and Z for each test case
    w, x, y, z = map(int, input().split())
    
    # Calculate and print the final balance
    print(w + z * (x - y))