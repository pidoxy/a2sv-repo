t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    
    # if you don't have a number greater than x, it is not possible
    result = "YES"
    greater = 0
    lesser = 0
    
    for num in a:
        if num > x:
            greater += 1
        if num < x:
            lesser += 1
    
    
    if greater == n or lesser == n:
        print("NO")
    else:
        print("YES")