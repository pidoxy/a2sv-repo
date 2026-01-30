import collections

class Solution:
    def checkEqual(self, a, b) -> bool:
        hashA = collections.Counter(a)
        hashB = collections.Counter(b)
        
        return hashA == hashB
