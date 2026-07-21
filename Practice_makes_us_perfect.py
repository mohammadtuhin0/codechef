# Read the four integers from a single line
problems = list(map(int, input().split()))

# Initialize a counter
count = 0

# Iterate through each week's value
for p in problems:
    if p >= 10:
        count += 1

# Output the result
print(count)