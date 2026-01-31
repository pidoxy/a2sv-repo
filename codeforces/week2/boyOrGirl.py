name = input()

uniqueNameLength = len(set(name))

if uniqueNameLength % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")