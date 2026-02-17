t = int(input())

results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    evens = []
    odds = []
    
    for x in a:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)
    
    evens.sort(reverse=True) # O(n)
    odds.sort(reverse=True) # O(n)
    
    pref = [0] * (len(evens) + 1)
    for i in range(len(evens)):
        pref[i+1] = pref[i] + evens[i]
        
    cnt_evens = len(evens)
    cnt_odds = len(odds)
        
    ans = []
        
    for k in range(1, n + 1): #T -> O(n), 
        if cnt_odds == 0:
            ans.append("0")
            continue
        
        needed_evens = k - 1
            
        take_evens = min(needed_evens, cnt_evens)
        
        remaining_spots = needed_evens - take_evens
        
        if remaining_spots % 2 != 0:
            take_evens -= 1
        
        if take_evens < 0 or (1 + (k - 1 - take_evens)) > cnt_odds:
            ans.append("0")
        else:
            score = odds[0] + pref[take_evens]
            ans.append(str(score))
                
    
    print(*(ans))

