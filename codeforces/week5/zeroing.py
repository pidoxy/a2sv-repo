
n,k = list(map(int, input().split()))
a = list(map(int, input().split()))

minElement = min(a)
subtractVal = 0

a.sort()
newA =[a[0]]

for i in range(1, n):
    if a[i] == newA[-1]:
        continue
    newA.append(a[i])

if k >= len(newA):
    for j in range(len(newA)):
        print(newA[j] - subtractVal)
        subtractVal = newA[j]
else:
    for j in range(k):
        print(newA[j] - subtractVal)
        subtractVal = newA[j]

for _ in range(k - len(newA)):
    print(0)
    
    

