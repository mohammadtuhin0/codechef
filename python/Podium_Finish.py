# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read A and B as space-separated integers
    a, b = map(int, input().split())
    
    # Calculate and print the sum
    print(a + b)