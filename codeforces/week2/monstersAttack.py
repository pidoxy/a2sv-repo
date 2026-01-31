t = int(input()) 

for i in range(t):
    n, k = map(int, input().split())

    health = list(map(int, input().split()))
    coordinates = list(map(int, input().split()))

    monsters = []
    for i in range(n):
        monsters.append((abs(coordinates[i]), health[i]))
    
    monsters.sort(key=lambda p: p[0])

    total_health = 0
    possible = True
    
    for dist, health in monsters:
        total_health += health
        
        if total_health > dist * k:
            possible = False
            break
    
    if possible:
        print("YES")
    else:
        print("NO")



