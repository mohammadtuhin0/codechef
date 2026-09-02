t = int(input())

for _ in range(t):
    n = int(input())
    
    two_kg = n // 2
    one_kg = n % 2
    
    cost = two_kg * 30 + one_kg * 20
    print(cost)