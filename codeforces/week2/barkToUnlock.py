password = input()

n = int(input())

words = []

for i in range(n):
    words.append(input())

# check if word matches exactly
# check if last letter matches first letter in password and if last letter in password matches a first letter

result = [False, False]

for word in words: 
    if word == password:
        print("YES")
        exit()
    
    if word[-1] == password[0]:
        result[0] = True
    if word[0] == password[1]:
        result[1] = True
    
if result[0] and result[1]:
    print("YES")
else:
    print("NO")
    
    
