t = int(input())
for _ in range(t):
    X, Y = map(int, input().split())
    
    cost_disposable = 100 * X
    cost_cloth = 10 * Y
    
    # If cloth is cheaper or equal, choose Cloth
    if cost_cloth <= cost_disposable:
        print("Cloth")
    else:
        print("Disposable")