class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = list(reversed(sorted(stones)))
        l = len(s)
        
        while(l>2):
            if s[0]==s[1]:
                s = s[2:]
                l-=2
            else:
                diff = s[0]-s[1]
                if diff==1:
                    s = s[2:]+[1]
                else:
                    i = 2
                    while(i<l):
                        if diff>s[i]:
                            s = s[2:i]+[diff]+s[i:]
                            break
                        i+=1
                    if i==l:
                        s = s[2:]+[diff]
                l-=1
        if l==2:
            if s[0]==s[1]:
                return 0
            else:
                return s[0]-s[1]
        else:
            return  s[0] if l!=0 else 0