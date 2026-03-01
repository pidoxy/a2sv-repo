t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    
    # find the max value and check if it appears even times or odd
    
    Count = {}
    
    for num in a:
        Count[num] = Count.get(num, 0) + 1
    
    # there needs to be at least one odd freq appearance of a number
    
    dagi_wins = "NO"
    for val in Count.values():
        if val % 2 != 0:
            dagi_wins = "YES"
    print(dagi_wins)
        