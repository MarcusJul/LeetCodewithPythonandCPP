class Solution:
    def findComplement(self, num: int) -> int:
        
        def tobits(num):
            n = num
            ret = ''
            base = 2147483648 #2^31
            i = 0
            while(i<32):
                l, r = int(n//base), int(n%base)
                ret += str(l)
                n = r
                base //= 2
                i+=1
            return ret 

        def frombits(s):
            ret = 0 
            base = 2147483648
            i = 0
            while(i<32):
                ret+= int(s[i])*base
                base //= 2
                i+=1
            return int(ret)
        
        bits = tobits(num)
        rev_bits = ''
        flag = False
        for i in range(32):
            if bits[i]=='1':
                flag = True
                rev_bits += '0'    
            else:
                if flag:
                    rev_bits += '1'
                else:
                    rev_bits += '0'
        
        return frombits(rev_bits)