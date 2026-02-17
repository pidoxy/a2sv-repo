t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    
    # sort based on cost to share and number you can share to
    costCapacity = []
    
    totalCost = p
    remaining = n -1
    
    for i in range(n):
        if cost[i] < p:
            costCapacity.append((cost[i], a[i]))
    
    costCapacity.sort()
    
    for price, capacity in costCapacity:
        if remaining == 0:
            break
        
        totalCost += price * min(capacity, remaining)
        remaining -= min(capacity, remaining)
    
    if remaining > 0:
        totalCost += remaining * p    
    
    print(totalCost)
    
    
    
    
    
    

