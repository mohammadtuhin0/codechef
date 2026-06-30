# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the duration in seconds
    s = int(input())
    
    # Calculate and print the total worth
    # 24 frames/sec * 1000 words/frame = 24000 words/sec
    print(24000 * s)