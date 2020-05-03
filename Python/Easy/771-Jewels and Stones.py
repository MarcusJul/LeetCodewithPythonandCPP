class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}.fromkeys(J,0)
        for char in S:
            try:
                d[char]+=1
            except:
                pass
        return sum(d.values())