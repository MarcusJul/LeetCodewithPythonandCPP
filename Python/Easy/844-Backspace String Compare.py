class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        Ts, Ss = [],[]
        i=0
        ls = len(S)
        while(i<ls):
            if S[i]=='#':
                if len(Ss)!=0:
                    Ss = Ss[:-1]
            else:
                Ss.append(S[i])
            i+=1    
        i=0
        lt = len(T)
        while(i<lt):
            if T[i]=='#':
                if len(Ts)!=0:
                    Ts = Ts[:-1]
            else:
                Ts.append(T[i])
            i+=1
        
        lTs, lSs = len(Ts), len(Ss)
        if lTs!=lSs:
            return False
        else:
            i=0
            while(i<lTs):
                if Ss[i]!=Ts[i]:
                    return False
                i+=1
            return True