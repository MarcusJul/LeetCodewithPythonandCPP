class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        temp = []
        steps1, steps2 = k%l, l-(k%l)
        
        for i in range(0,l):
            if i<steps2:
                temp.append(nums[i])
            else:
                nums[i-steps2] = nums[i]
        for i in range(l-steps2,l):
            nums[i] = temp[i-steps1]