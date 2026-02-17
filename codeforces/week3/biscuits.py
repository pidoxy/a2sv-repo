t = int(input())

for i in range(t):
    n = int(input())
    
    result = 0
    
    if n % 2 == 0:
        result = (n //2) - 1
    else:
        result = n // 2

    print(result)
        