# Function to process each test case
def solve():
    # Read W, X, Y, Z for a single test case
    w, x, y, z = map(int, input().split())
    
    # Calculate the total water in the bucket
    total_water = w + (y * z)
    
    # Compare with capacity X and print the result
    if total_water > x:
        print("overflow")
    elif total_water == x:
        print("filled")
    else:
        print("unfilled")

def main():
    # Read the number of test cases
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()