n,k = list(map(int, input().split()))

a = list(map(int, input().split()))

# print(n,k)

a.sort()

# print(a)

# print(a[k])

if a[k] != a[k-1]:
    print(a[k]-1) 
else:
    print(-1)