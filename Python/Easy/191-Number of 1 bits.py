class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        count = 0
        i= 31
        while(i>=0):
            left, right = n//2**i, n%2**i    
            if left==1:
                count+=1
            n=right
            i-=1
        return count
        