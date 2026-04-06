import sys

input_data = sys.stdin.read().split()

t = int(input_data[0])
idx = 1

results = []

for _ in range(t):
    n = int(input_data[idx])
    m = int(input_data[idx+1])
    idx += 2
    
    if n == 1 and m == 1:
        results.append("-1")
        idx += 1  
        continue
        
    flat_grid = []
    for _ in range(n * m):
        flat_grid.append(input_data[idx])
        idx += 1
        
    flat_grid = [flat_grid[-1]] + flat_grid[:-1]
    
    k = 0
    for _ in range(n):
        results.append(" ".join(flat_grid[k : k + m]))
        k += m
        
print("\n".join(results))