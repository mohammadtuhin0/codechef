# Accept the number of test cases
T = int(input())

for _ in range(T):
    # Read N (number of colors)
    N = int(input())
    
    # Read the array of ball counts, convert them to integers, 
    # and print the maximum value
    A = list(map(int, input().split()))
    print(max(A))