import sys


def solve():
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    T = int(data[0])
    idx = 1
    out = []

    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = [int(data[idx + i]) for i in range(N)]
        idx += N

        # The maximum number of breaks is (sum of all lengths) - N
        ans = sum(A) - N
        out.append(str(ans))

    print("\n".join(out))


if __name__ == "__main__":
    solve()
