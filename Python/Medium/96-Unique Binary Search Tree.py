# first solution one
class Solution:
    def numTrees(self, n: int) -> int:
        if n==0:
            return 1
        def countn(n):
            if n<3:
                return n
            else:
                count = 0
                for left in range(int(n/2)):
                    count+=max(1,countn(left))*max(1,countn(n-1-left))
                count*=2
                if n%2==1:
                    oneside = max(1,countn(int(n/2)))
                    count+=oneside**2
                return count
            
        return countn(n)
    
# sec solution
class Solution:
    def numTrees(self, n: int) -> int:
        if n==0:
            return 1
        def countn(n, lib):
            if n in lib:
                return lib[n], lib
            else:
                count = 0
                rlib = lib
                for left in range(int(n/2)):
                    lefttree, rlib = countn(left,rlib)
                    
                    righttree, rlib = countn(n-1-left,rlib)
                    count+=max(1,lefttree)*max(1,righttree)
                count*=2
                if n%2==1:
                    oneside,rlib = countn(int(n/2),rlib)
                    if oneside<1:
                        oneside=1
                    count+=oneside**2
                lib[n] = count
                return count, rlib
        count, lib = countn(n, {0:0,1:1,2:2})
        return count