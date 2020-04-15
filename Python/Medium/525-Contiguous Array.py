class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        s = 0
        l = len(nums)
        d = {0:-1}
        m = 0
        for i in range(l):
            s += 1 if nums[i]==1 else -1
            if s not in d:
                d[s] = i
            else:
                if i-d[s]>m:
                    m = i-d[s]
        return m
        
        