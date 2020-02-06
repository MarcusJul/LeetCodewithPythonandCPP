class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        def binary(left, right):
            f = int((left+right)/2)
            if f*f>x: # larger than proper
                if (f-1)*(f-1)<=x:
                    return f-1
                else:
                    return binary(left, f)
            elif f*f<x:
                if (f+1)*(f+1)>=x:
                    return f
                else:
                    return binary(f+1, right)
            else:
                return f
        
        return binary(0,x)
            
            
#################################################

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        else:
            sf = 1
            while(True):
                if sf*sf<=x:
                    pass
                else:
                    return sf-1
                sf+=1