t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    
    found = False
    res = []
    
    for i in range(1, n-1):
        if h[i-1] < h[i] and h[i] > h[i+1]:
            found = True
            res = [i,i+1,i+2]
            break
    if found:
        print("YES")
        print(res[0], res[1], res[2])
    else:
        print("NO")