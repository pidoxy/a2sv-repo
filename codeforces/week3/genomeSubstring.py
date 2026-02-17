n = int(input())
s = input()

target = "ACTG"
min_ops = float('inf')

# Check every substring of length 4 in s
for i in range(n - 3):
    substring = s[i : i+4]
    current_ops = 0
    
    for j in range(4):
        # Calculate linear distance between characters
        dist = abs(ord(substring[j]) - ord(target[j]))
        # Take the shorter path: direct or wrapping around (cyclic)
        cost = min(dist, 26 - dist)
        current_ops += cost
    
    # Update the minimum operations found so far
    if current_ops < min_ops:
        min_ops = current_ops

print(min_ops)