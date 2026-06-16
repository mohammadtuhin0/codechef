# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read X, Y, and Z from the input line
    x, y, z = map(int, input().split())
    
    # Calculate total credits
    total_credits = (x * 4) + (y * 2) + (z * 0)
    
    # Print the result
    print(total_credits)