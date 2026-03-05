n, m = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

merged = []
i, j = 0,0
while i < n and j < m:
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        elif a[i] > b[j]:
            merged.append(b[j])
            j += 1
print(merged)