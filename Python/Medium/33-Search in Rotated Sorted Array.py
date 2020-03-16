class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==[]:
            return -1
        if len(nums)==1:
            return 0 if nums[0]==target else -1
            
        left, right = 0, len(nums)-1
        def slice(tar, left, right):
            if left==right-1:
                if nums[left]==tar:
                    return left
                elif nums[right]==tar:
                    return right
                else:
                    return -1
            
            mid = int((left+right)/2)
            
            if nums[mid]==tar:
                return mid
        
            if nums[left]<nums[mid]:#left is ascending
                if tar>nums[left] and tar<nums[mid]:
                    return slice(tar, left, mid)
                elif nums[left]==tar:
                    return left
                elif nums[mid]==tar:
                    return mid
                else:
                    return slice(tar, mid, right)
            else:# right is ascending
                if tar>nums[mid] and tar<nums[right]:
                    return slice(tar, mid, right)
                elif tar==nums[mid]:
                    return mid
                elif tar==nums[right]:
                    return right
                else:
                    return slice(tar, left, mid)
        
        return slice(target, left, right)