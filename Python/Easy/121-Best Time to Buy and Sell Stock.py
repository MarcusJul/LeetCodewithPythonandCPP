class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==[]:
            return 0
        revmax = []
        m = -1
        l = len(prices)
        for i in range(l):
            m = max(prices[l-1-i],m)
            revmax = [m] + revmax
        
        ret = -1
        for i in range(l):
            ret = max(ret, revmax[i]-prices[i])
        return ret