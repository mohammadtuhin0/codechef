# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read X and Y for each test case
    x, y = map(int, input().split())
    
    # Calculate total tastiness
    chocolate_tastiness = 2 * x
    candy_tastiness = 5 * y
    
    # Compare and print the result
    if chocolate_tastiness > candy_tastiness:
        print("Chocolate")
    elif candy_tastiness > chocolate_tastiness:
        print("Candy")
    else:
        print("Either")