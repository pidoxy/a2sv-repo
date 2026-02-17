t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    unique = len(set(a))
    
    print((2 * unique) - 1)