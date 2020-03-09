class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for k,v in d.items():
            if v==1:
                return k