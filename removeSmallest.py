t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    
    a.sort()
    result = n
    
    for i in range(1, n):
        if (a[i] - a[i-1]) <= 1:
            result -= 1
    if result == 1:
        print("YES")
    else:
        print("NO")