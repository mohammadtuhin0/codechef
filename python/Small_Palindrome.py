t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    
    left = "1" * (x // 2) + "2" * (y // 2)
    answer = left + left[::-1]
    print(answer)