class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        temp = []
        while(i<len(nums)):
            if nums[i]!=val:
                temp.append(nums[i])
            i+=1
        nums[:len(temp)] = temp
        return len(temp)