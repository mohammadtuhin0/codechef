t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = {}
    
    for x in a:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
        
    max_freq = max(freq.values())
    answer = n - max_freq
    print(answer)