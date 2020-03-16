class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        oldr = len(nums)
        ravel = []
        for i in range(oldr):
            ravel+=nums[i]
        
        
        rm = []
        if r*c>len(ravel):
            return nums
        
        for row in range(r):
            rm.append(ravel[row*c:(row+1)*c])
        
        return rm