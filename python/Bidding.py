# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the three bids
    A, B, C = map(int, input().split())
    
    # Find the maximum value among the three
    winner_bid = max(A, B, C)
    
    # Check whose bid matches the maximum
    if winner_bid == A:
        print("Alice")
    elif winner_bid == B:
        print("Bob")
    else:
        print("Charlie")