class Solution:
    # Devide and conquer, with O(n*log(n)) complexity
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        midpoint = int(l/2)
        return max(self.maxSubArray(nums[0:midpoint]),
                  self.maxSubArray(nums[midpoint:]),
                  self.maxmidsum(nums,midpoint,l))

    # Used in divide and conquer
    def maxmidsum(self,nums,midpoint,l):
        if l==1:
            return nums[0]
        elif l==2:
            return max(max(nums),sum(nums))
        else:
            pass
        
        # left sum
        leftsum = nums[midpoint-1]
        flag = False
        tempsum = 0
        for i in range(midpoint-2,-1,-1):
            if nums[i]>=0:
                if flag == True:
                    if nums[i]+tempsum >= 0:
                        leftsum += tempsum + nums[i]
                        tempsum = 0
                        flag = False
                    else:
                        tempsum += nums[i]
                else:
                    leftsum += nums[i]
            else:
                if flag == True:
                    pass
                else:
                    flag = True
                tempsum += nums[i]
        
        # right sum
        rightsum = nums[midpoint]
        flag = False
        tempsum = 0
        for i in range(midpoint+1,l):
            if nums[i]>=0:
                if flag == True:
                    if nums[i]+tempsum >= 0:
                        rightsum += tempsum + nums[i]
                        tempsum = 0
                        flag = False
                    else:
                        tempsum += nums[i]
                else:
                    rightsum += nums[i]
            else:
                if flag == True:
                    pass
                else:
                    flag = True
                tempsum += nums[i]
        #print(leftsum, rightsum, nums,sum(nums))
        return leftsum+rightsum
        
    # Complexity O(n)
    def ncomp(self, nums: List[int])->int:
        
        maxsum, cursum = 0,0
        for i in range(len(nums)):
            cursum += nums[i]
            if cursum<0:
                cursum = 0
            else:
                maxsum = max(maxsum,cursum)
        if max(nums)<0:
            return max(nums)
        else:
            return maxsum 
                
        
        