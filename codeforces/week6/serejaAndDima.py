n = int(input())

cards = list(map(int, input().split()))

l, r = 0, n-1

sereja, dima = 0, 0

for i in range(n):
    if i % 2 == 0:
        if cards[l] > cards[r]:
            sereja += cards[l]
            l += 1
        else:
            sereja += cards[r]
            r -= 1
    else:
        if cards[l] > cards[r]:
            dima += cards[l]
            l += 1
        else:
            dima += cards[r]
            r -= 1
        
print(sereja, dima)
