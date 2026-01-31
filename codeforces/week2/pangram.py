n = int(input())

word = input()


if n < 26:
    print("NO")
    exit()

container = set()

for char in word:
    container.add(ord(char.lower()))

if len(container) == 26:
    print("YES")
else:
    print("NO")

