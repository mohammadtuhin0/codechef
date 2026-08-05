import math

# Read the number of test cases
t = int(input())

for _ in range(t):
    n = int(input())
    
    # Find the integer square root of n using math.isqrt()
    b = math.isqrt(n)
    
    # Output the square of b
    print(b * b)