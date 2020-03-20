class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        def to_bits(n):
            ret = ''
            i = 31
            
            while(i>=0):
                left, right = n//2**i, n%2**i    
                ret+=str(left)
                n=right
                i-=1
            
            return ret
        bits = to_bits(n)
        rbits = ''.join([bit for bit in reversed(bits)])
        
        print(rbits, type(rbits))
        s = 0
        for i in range(32):
            s+=int(rbits[i])*(2**(31-i))
        return s