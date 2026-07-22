# Read N and M from the input
n, m = map(int, input().split())

# Check if errors are present in at least half of the total lines
if m >= n / 2:
    print("NEWBIE")
else:
    print("PRO")