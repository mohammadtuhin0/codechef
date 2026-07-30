# Read N
n = int(input())

# Read the list of weapons
weapons = list(map(int, input().split()))

# Count how many soldiers have an even number of weapons
even_count = 0
for w in weapons:
    if w % 2 == 0:
        even_count += 1

# Odd count is total soldiers minus even count
odd_count = n - even_count

# Check the condition
if even_count > odd_count:
    print("READY FOR BATTLE")
else:
    print("NOT READY")