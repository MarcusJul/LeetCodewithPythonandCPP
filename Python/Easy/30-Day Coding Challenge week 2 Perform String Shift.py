class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if len(shift)==0:
            return s
        count = 0
        for pair in shift:
            count += pair[1] if pair[0]==0 else -pair[1]
        print(count)
        l = len(s)
        return s[count%l:]+s[:count%l]
        