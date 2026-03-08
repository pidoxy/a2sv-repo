t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    
    crowd = a[n-1] + a[n-2]
    elite = a[0]
    
    if n % 2 == 0:
        mid = n // 2
    else:
        mid = (n // 2) + 1
        
    # print(mid)
    result = "NO"
    l = 1
    r = n-3
    
    while True:
        if elite > crowd:
            result = "YES"
            break
        
        if r < l:
            break
        
        elite += a[l]
        crowd += a[r]
        l += 1
        r -= 1
    
    print(result)
