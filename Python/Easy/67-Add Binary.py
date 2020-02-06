class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        #lena, lenb = len(a), len(b)
        #ll = max(lena,lenb)
        def BinarytoInt(s):
            s = int(s)
            counter,ssum = 0, 0
            while(s>=1):
                ssum += (2**counter) * (s%10)
                s = s//10
                counter+=1
            return ssum
        
        def InttoBinary(i):
            if i>=1:
                out = ''
                while(i>=1):
                    out = str(int(i%2))+out
                    i = i//2
            else:
                out = "0"
            return out
        ia, ib = BinarytoInt(a), BinarytoInt(b)
        iab, ibb = InttoBinary(ia), InttoBinary(ib)
        sumab = InttoBinary(ia+ib)
        return sumab