class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def merge(nums):
            l = len(nums)
            if l>2:
                left = merge(nums[:int(l/2)])
                right = merge(nums[int(l/2):])
                i, j = 0,0
                ret = []
                while(i!=len(left) and j!=len(right)):
                    if left[i]<right[j]:
                        ret.append(left[i])
                        i+=1
                    else:
                        ret.append(right[j])
                        j+=1
                if i==len(left):#right is left
                    ret += right[j:]
                else:
                    ret += left[i:]
                return ret
            elif l==2:
                if nums[0]<nums[1]:
                    return nums
                else:
                    return [nums[1],nums[0]] 
            else:
                return nums
                
                
        n, m = len(nums1),len(nums2)
        left, right = nums1, nums2
        
        i, j = 0,0
        nums = []
        while(i!=len(left) and j!=len(right)):
            if left[i]<right[j]:
                nums.append(left[i])
                i+=1
            else:
                nums.append(right[j])
                j+=1
        if i==len(left):#right is left
            nums += right[j:]
        else:
            nums += left[i:]
        
        #nums = merge(nums1+nums2) # You can use the above merge function also
        if (n+m)%2==0:
            if n+m==0:
                return None
            mid = int((n+m)/2)
            return (nums[mid-1]+nums[mid])/2
        else:
            return nums[int((n+m)/2)]
            
        
            
            