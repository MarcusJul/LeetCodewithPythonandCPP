# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1,n
        
        d = {}
        
        while(True):
            mid = int((left+right)/2)
            if left==right:
                break
            
            if mid in d:
                v = d[mid]
            else:
                v = isBadVersion(mid)
                d[mid] = v
                
            if v:
                if mid>=1:
                    if mid-1 in d:
                        v = d[mid-1]
                        if v==False:
                            break
                        else:
                            right = mid-1
                    else:
                        v = isBadVersion(mid-1)
                        d[mid-1] = v
                        if v==False:
                            break
                        else:
                            right = mid-1
                else:
                    mid = 0
                    break
            else:
                if mid<=n-1:
                    if mid+1 in d:
                        v = d[mid+1]
                        if not v:
                            left = mid+1
                        else:
                            mid += 1
                            break
                    else:
                        v = isBadVersion(mid+1)
                        d[mid+1] = v
                        if not v:
                            left = mid+1
                        else:
                            mid += 1
                            break
                
                else:
                    print('Boundary condition!')
                    break
                    
        return mid