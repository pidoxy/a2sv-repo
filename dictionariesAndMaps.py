# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(sys.stdin.readline().strip())
        
# Step 2: Build the dictionary
phone_book = {}
for _ in range(n):
    entry = sys.stdin.readline().split()
    phone_book[entry[0]] = entry[1]

# Step 3: Read queries until EOF
queries = sys.stdin.readlines()

for q in queries:
    name = q.strip()
    if name in phone_book:
        print(f"{name}={phone_book[name]}")
    else:
        print("Not found")
    
        
