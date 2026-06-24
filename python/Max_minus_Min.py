# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read A, B, and C as integers
    a, b, c = map(int, input().split())
    
    # Since A < B < C, the answer is always C - A
    print(c - a)