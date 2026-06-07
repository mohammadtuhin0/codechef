# cook your dish here
# Read the input values X and Y
x, y = map(int, input().split())

# Check if the total distance (x * y) is at least 100
if x * y >= 100:
    print("Yes")
else:
    print("No")