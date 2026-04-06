from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    
    n,k = map(int, input().split())
    brand_totals = defaultdict(int)
    
    for _ in range(k):
        b,c = map(int, input().split())
        
        brand_totals[b] += c
        
    sorted_totals = sorted(brand_totals.values(), reverse=True)
    
    result = sum(sorted_totals[:n])
    
    print(result)
        
    
    
    


