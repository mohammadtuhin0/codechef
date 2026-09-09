x, y, f = map(int, input().split())

shop1 = x * 12
shop2 = y * 12 + f

if shop1 < shop2:
    print(shop1)
else:
    print(shop2)