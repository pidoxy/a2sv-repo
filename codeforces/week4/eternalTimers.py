t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    result = "YES"
    for i in range(n):
        if (a[i] <= (n - (i+1)) * 2):
            result = "NO"
        
        if (a[i] <= (i * 2)):
            result = "NO"
            
    print(result)