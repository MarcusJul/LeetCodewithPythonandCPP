class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        i = 0
        rep = {}
        while(i<len(s)):
            if s[i] in rep:
                if rep[s[i]]==t[i]:
                    pass
                else:
                    return False
            else:
                rep[s[i]] = t[i]
            i+=1
        vlst = list(rep.values())
        
        cd = dict.fromkeys(vlst,0)
        if len(cd.keys())==len(vlst):
            return True
        else:
            return False
        