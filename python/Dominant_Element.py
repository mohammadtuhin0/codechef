# Loop through each test case
for _ in range(int(input())):
    n = int(input())  # Read the number of elements in the current test case
    a = list(map(int, input().split()))  # Read the elements into a list

    # Create a frequency list initialized to zero with size n+1
    freq = [0] * (n + 1)

    # Count the frequency of each element in the list
    for x in a:
        freq[x] += 1  # Increment the count for element  x

    # Find the maximum frequency of any element in the list
    mx = max(freq)

    # Check if there is exactly one element with the maximum frequency
    print('yes' if freq.count(mx) == 1 else 'no')