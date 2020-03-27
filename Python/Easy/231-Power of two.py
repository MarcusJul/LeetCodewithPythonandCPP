class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return None
        if n==1:
            return True
        
        
        while(True):
            if n%2==1:
                return False
            else:
                n/=2
            if n==1:
                return True
        