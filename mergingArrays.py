
n,m = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_array = []

p1, p2 = 0,0

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        sorted_array.append(a[p1])
        p1 += 1
    else:
        sorted_array.append(b[p2])
        p2 += 1
else:
    while p1 < n:
        sorted_array.append(a[p1])
        p1 += 1
    while p2 < m:
        sorted_array.append(b[p2])
        p2 += 1

print(sorted_array)