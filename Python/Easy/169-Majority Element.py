class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        ret = None
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            if d[num]>=n/2:
                ret = num
                break
        if ret!=None:
            return ret
        else:
            pass