T = int(input())

for _ in range(T):
    p, q = map(int, input().split())
    total_serves = p + q
    turn = total_serves // 2
    
    if turn % 2 == 0:
        print("Alice")
    else:
        print("Bob")