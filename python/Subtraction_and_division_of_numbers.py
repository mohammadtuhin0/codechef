t = int(input())
for i in range(t):
    a, b = map(int,input().split())     
    diff = a - b 
    division = a // b 
    
    print(diff, division)
