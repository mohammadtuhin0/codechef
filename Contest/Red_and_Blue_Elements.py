t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    total = sum(a)

    prefix = 0
    answer = 0

    for k in range(1, n):
        prefix += a[k - 1]

        sr = prefix
        sb = total - sr

        cr = k
        cb = n - k

        value = sr * cb + sb * cr

        answer = max(answer, value)

    print(answer)