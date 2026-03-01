t = int(input())

for _ in range(t):
    n = int(input())
    
    pairs = []
    
    for _ in range(n):
        
        a, b = list(map(int, input().split()))
        pairs.append((a,b))
        
    pairs.sort(key=lambda x: (sum(x), x[0]))
    
    result = []
    
    for a,b in pairs:
        result.append(a)
        result.append(b)
    
    print(*result)

