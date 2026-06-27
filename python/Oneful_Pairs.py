# Read the two space-separated integers
a, b = map(int, input().split())

# Check the condition given in the problem
if a + b + (a * b) == 111:
    print("Yes")
else:
    print("No")