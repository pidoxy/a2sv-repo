t = int(input())

for i in range(t):
    n = int(input())
    
    if n == 2:
        print(2)
    elif n == 3:
        print(3)
    else:
        # For n >= 4:
        # If n is even, diff is 0. 
        # If n is odd, diff is 1.
        print(n % 2)