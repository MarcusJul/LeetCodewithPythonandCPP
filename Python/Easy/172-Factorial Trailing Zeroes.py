class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        def countn(n, base):
            
            tcount = 0
            b = base
            while(b<=n):
                tcount+=n//b
                b*=base
                
            return tcount
        
        count2, count5 = countn(n,2),countn(n,5)
        print(count2, count5)
        return min(count2, count5)