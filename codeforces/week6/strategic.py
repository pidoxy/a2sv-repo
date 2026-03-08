t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    total = sum(a)
    
    for i in range(k):
        diff = 0
        for j in range(n-b[i]):
            tmp = a[j:j+b[i]]
            minCost = min(tmp)
            print(minCost, "min")
            diff = max(diff, minCost)
        a.remove(diff)
        total -= diff
    print(total)
            