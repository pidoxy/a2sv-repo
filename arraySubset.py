#User function Template for python3
import collections

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        hash = collections.Counter(a)
        
        for num in b:
            if hash[num] == 0:
                return False
            hash[num] -= 1
        
        return True
    
    
    
    
