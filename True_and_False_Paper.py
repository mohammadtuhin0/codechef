# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read N and K
    n, k = map(int, input().split())
    
    # Bob's score is the number of questions Alice got wrong
    print(n - k)