n, a, m, b = map(int, input().split())
bought = n * a
sold = m * b

profit = sold - bought
print(profit)