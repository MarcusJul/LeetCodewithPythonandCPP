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
            
# Solution 2            
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l==0 or l==1:
            return nums
        
        
        
        # repeat the process of swap the next non-zero number with the first zero in the checked array
        # swap and create first moved array first
        ni,zi = None,None # zi is the index of next zero in the moved array, ni is the index of the last non-zero in array
        # Find the last non-zero before 0
        # i.e. 10004,01234,12340 and 000040, you need to return the index of 4 
        flag=False
        for i,num in enumerate(nums):
            if num!=0:
                ni = i
                break
                
        for i,num in enumerate(nums):
            if num==0:
                zi = i
                break
                
        if zi==None or ni==None:
            return 
        # Now you have found the first 0 and first non-0
        # There are 2 scenarios: a bunch of(could be 1) 0s then non-zero
        # and a bunch of (could be 1) non-zero then 1
        if zi<ni: # a bunch of zero comes first
            nums[zi], nums[ni] = nums[ni], nums[zi]
            zi += 1
            i = ni + 1
        else:
            i = zi + 1
            
        while(i<l):
            if nums[i]!=0:
                nums[i], nums[zi] = nums[zi],nums[i]
                zi+=1
            i+=1
        return
            
            
            