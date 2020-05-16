class Solution:
    def firstUniqChar(self, s: str) -> int:
        notrep = {}
        rep = {}
        for i, char in enumerate(s):
            if char not in rep:
                notrep[char] = i
                rep[char] = i
            else:
                notrep[char] = -1
                
        for k,v in notrep.items():
            if v!=-1:
                return v
        return -1