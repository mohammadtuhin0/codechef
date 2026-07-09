# Read input as a string and split into X and Y
input_data = input().split()
x = int(input_data[0])
y = float(input_data[1])

# Check if withdrawal is a multiple of 5 AND if there is enough balance
if x % 5 == 0 and (x + 0.50) <= y:
    y = y - x - 0.50

# Print the final balance formatted to 2 decimal places
print(f"{y:.2f}")