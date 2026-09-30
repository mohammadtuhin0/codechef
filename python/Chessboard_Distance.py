import sys

def solve():
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    distance = max(abs(x1 - x2), abs(y1 -y2))
    print(distance)
    
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
        
        
if __name__ == '__main__':
    main()