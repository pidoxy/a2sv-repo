n = int(input())

cards = list(map(int, input().split()))

serejaScore = 0
dimaScore = 0

turns = 0

l, r = 0, n-1
while turns < n:
    if turns % 2 == 0:
        serejaScore += max(cards[l], cards[r])

        if cards[l] > cards[r]:
            l += 1 
        else: 
            r -= 1 
    else: 
        dimaScore += max(cards[l], cards[r]) 

        if cards[l] > cards[r]:
            l += 1 
        else: 
            r -= 1 

    turns += 1
print(serejaScore, dimaScore)
    