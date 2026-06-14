x, y, z = map(int, input().split())

answer = x - y
if answer <= z:
    print("Yes")
else:
    print("No")