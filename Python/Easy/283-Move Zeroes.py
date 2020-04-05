# Solution 1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        
        
        container = []
        count = 0
        for i,num in enumerate(nums):
            if num!=0:
                container.append(num)
                count+=1
        
        for i in range(count):
            nums[i] = container[i]
        for i in range(count,len(nums)): 
            nums[i]=0
            
        return
            

            
            
            