F1, P1, F2, P2 = map(int, input().split())

first = abs(F1 - P1)
second = abs(F2 - P2)

if first < second:
    print("First")
elif second < first:
    print("Second")
else:
    print("Both")