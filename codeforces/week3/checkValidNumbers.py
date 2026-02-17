t = int(input())

for i in range(t):
    # Read all 4 integers from the single line
    n, m, p, q = map(int, input().split())
    
    result = ""
    
    # Check if the array length (n) is a perfect multiple of the segment length (p)
    if n % p == 0:
        # If it is, the total sum (m) MUST be exactly (n / p) * q
        if m == (n // p) * q:
            print("YES")
        else:
            print("NO")
    else:
        # If there is a remainder, we can always balance the array using negative numbers
        print("YES")

