class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def to_bits(n):
            i = 31
            ret = ''
            flag = False
            while(i>=0):
                left, right = n//2**i, n%2**i
                ret += str(left)
                n = right
                i-=1
            print(ret)
            return ret
        
        xbits, ybits = to_bits(x),to_bits(y)
        count = 0
        for i in range(len(xbits)):
            if (xbits[i]=='1' and ybits[i]=='1') or (xbits[i]=='0' and ybits[i]=='0'):
                pass
            else: 
                count+=1
                
        
        return count #abs(xbits-ybits)