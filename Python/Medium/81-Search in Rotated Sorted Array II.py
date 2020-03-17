class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums==[]:
            return False
        if len(nums)==1:
            return True if nums[0]==target else False
            
        left, right = 0, len(nums)-1
        def slice(tar, left, right):
            if left==right-1:
                if nums[left]==tar:
                    return True
                elif nums[right]==tar:
                    return True
                else:
                    return False
            
            mid = int((left+right)/2)
            
            if nums[mid]==tar or nums[left]==tar or nums[right]==tar:
                return True
            else:
                return slice(tar, left, mid) or slice(tar, mid, right)
        
        return slice(target, left, right)