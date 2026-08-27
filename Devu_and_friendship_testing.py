t = int(input())

for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    print(len(set(d)))