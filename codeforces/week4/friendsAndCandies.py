t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = sum(a)
    
    if total % n != 0:
        print(-1)
        continue
    
    avg = total // n
    
    result = n
    
    for i in range(n):
        if avg == a[i]:
            result -= 1
        elif avg > a[i]:
            result -= 1
    
    print(result)
    
    