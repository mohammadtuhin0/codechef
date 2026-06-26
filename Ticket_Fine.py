t = int(input())

for _ in range(t):
    x, p, q = map(int, input().split())
    without_ticket = p - q
    t_fine = without_ticket * x
    print(t_fine)