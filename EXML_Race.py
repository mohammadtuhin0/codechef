import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    T = int(data[0])
    idx = 1
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        
        # Read the first car's data to initialize our best car tracker
        d, t = int(data[idx]), int(data[idx+1])
        idx += 2
        
        best_speed = d // t
        best_car = 1  # Car labels are 1-indexed
        
        # Check the rest of the cars
        for i in range(2, N + 1):
            d, t = int(data[idx]), int(data[idx+1])
            idx += 2
            
            current_speed = d // t
            
            # Update only if strictly greater to keep the minimum label in case of ties
            if current_speed > best_speed:
                best_speed = current_speed
                best_car = i
                
        print(best_car)

if __name__ == '__main__':
    solve()
