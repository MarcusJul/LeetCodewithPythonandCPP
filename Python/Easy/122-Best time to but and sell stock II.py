class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==[]:
            return 0
        
        l = len(prices)
        si, ei = 0,0 
        i = 0
        s = 0
        while(i<l-1):
            if prices[i+1]<=prices[i]:
                i+=1
            else:
                si,ei = i,i+1
                while(ei<l and prices[ei]>=prices[ei-1]):
                     ei+=1
                s += prices[ei-1]-prices[si]
                i = ei
        
        return s