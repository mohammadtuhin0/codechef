T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    entry = A[0]
    total_wait = 0

    for i in range(1, N):
        entry = max(entry, A[i])
        total_wait += entry - A[i]

    print(total_wait)