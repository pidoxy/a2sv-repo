t = int(input())

for _ in range(t):
    s = input()
    working_keys = set()
    
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        
        block_length = j - i
        
        if block_length % 2 != 0:
            working_keys.add(s[i])
        
        i = j
        
    res = "".join(sorted(working_keys))
    print(res)
            