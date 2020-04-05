class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fi, li = -1, -1
        flag = False
        if nums==[]:
            return [-1,-1]
        l = len(nums)
        # Find left fi
        left, right = 0, l-1
        def findtar(left, right):
            if right-left<=1:
                return left if nums[left]==target else right
            mid = int((left+right)/2)
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]<target:
                    return findtar(mid,right)
                else:
                    return findtar(left,mid)
                
        def findleft(left, right): #nums[right] = target
            if nums[left]==target:
                return left
            if right-left<=1:
                return right
            mid = int((left+right)/2)
            if nums[mid]==target:
                if mid-1>=0:
                    if nums[mid-1]!=target:
                        return mid
                    else:
                        return findleft(left,mid-1)
                else:
                    return mid
            else:
                if right-1>=0:
                    if nums[right-1]!=target:
                        return right
                    else:
                        return findleft(mid, right-1)
                else:
                    return right

        def findright(left, right): #nums[left] = target
            if nums[right]==target:
                return right
            if right-left<=1:# 2 numbers
                return left

            mid = int((left+right)/2)
            if nums[mid]==target:
                if mid+1<l:
                    if nums[mid+1]!=target:
                        return mid
                    else:
                        return findright(mid+1,right)
                else:
                    return mid
            else:
                if left+1<l:
                    if nums[left+1]!=target:
                        return left
                    else:
                        return findright(left+1, mid)
                else:
                    return left
        mid = findtar(left, right)
        if nums[mid]!=target:
            return [-1,-1]
        # Find the left boundary
        if mid-1>=0:
            if nums[mid-1]!=target:
                fi = mid
            else:
                fi = findleft(left, mid-1)
        else:
            fi = findleft(left, mid)

        if mid+1<l:
            if nums[mid+1]!=target:
                li = mid
            else:
                li = findright(mid+1, right)
        else:
            li = findright(mid, right)
        print(nums)
        print(fi,li)
            
        return [fi,li]
                    
                    