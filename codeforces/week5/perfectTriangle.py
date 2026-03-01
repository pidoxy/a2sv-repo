t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # keep appearance freq of each number
    # if one appears 3 or more times, the result is 0
    # if one appears twice, the difference in the nearest number to that number is the answer
    # if all appear once, 
    a.sort()
    result = float('inf')
    
    for i in range(1, n-1):
        result = min(result, abs(a[i]-a[i-1]) + abs(a[i]-a[i+1]))
    print(result)
    
        
    