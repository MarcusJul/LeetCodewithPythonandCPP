class Solution:
    def isHappy(self, n: int) -> bool:
        def divandcon(n,lib):
            digits = []
            num = n
            while(num>0):
                digits = [num%10] + digits
                num//=10
            s = sum([i**2 for i in digits])
            if s==1:
                return True
            else:
                if s in lib:
                    return False
                else:
                    lib.append(s)
                    return divandcon(s, lib)
        return divandcon(n, [])