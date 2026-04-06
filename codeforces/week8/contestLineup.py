t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    unbalanced = 0
    
    i0, i1 = 0,0
    
    while max(i0,i1) < n:
        if b[i1] < a[i0]:
            i1 += 1
        else:
            i0 += 1
            i1 += 1
    print(n - i0)