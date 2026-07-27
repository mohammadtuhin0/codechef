for _ in range(int(input())):
    r1, r2, r3 = map(int, input().split())
    
    # Check if any company's revenue is strictly greater than the sum of the other two
    if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
        print("YES")
    else:
        print("NO")