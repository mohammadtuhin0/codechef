for _ in range(int(input())):
    x, y, z = map(int, input().split())
    # 24 * 60 is the number of minutes in a single day (1440)
    if x * y <= 24 * 60 * z:
        print("YES")
    else:
        print("NO")