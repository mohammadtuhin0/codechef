money = int(input())

x, b = map(int,input().split())

if money >= (x + b):
    print("Yes")
else:
    print("No")