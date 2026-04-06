t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    mismatches = []
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            mismatches.append(i)
    
    if not mismatches:
        print("YES")
        continue
    
    # check if mismatched indices are contiguous, if they are, [l, r] can be set, else print("NO")
    
    is_contiguous = True
    for i in range(1, len(mismatches)):
        if mismatches[i] - mismatches[i-1] > 1:
            is_contiguous = False
    
    if is_contiguous:
        print("YES")
    else:
        print("NO")
    