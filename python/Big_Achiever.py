T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    max_score = 0
    result = []

    for i in range(N):
        if A[i] > max_score:
            result.append(1)
            max_score = A[i]
        else:
            result.append(0)

    print(*result)