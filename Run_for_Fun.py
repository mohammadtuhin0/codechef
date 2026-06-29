# Read X and Y from input
x, y = map(int, input().split())

# We use (y-1) // x to account for the case where 
# y is an exact multiple of x (where he doesn't need a final rest)
print((y - 1) // x)