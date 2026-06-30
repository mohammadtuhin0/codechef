# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the spice level X
    x = int(input())
    
    # Check the categories based on the given constraints
    if x < 4:
        print("MILD")
    elif x < 7:
        print("MEDIUM")
    else:
        print("HOT")