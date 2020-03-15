class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start from the end of the list
        # check whether you can move the current list to next permutation, if you can't, move on
        
        
        def nextPer(lst,
                    nn, #new num
                    i, # i is the start of the lst 
                   ):
            # Check if the with the new number the list can arrange next permu
            # if the nn is less than any of them, then it is possible
            # alternatively, if the nn is larger then any one of them, recursively you will always have a decsending array on the left
            print(lst)
            ind, l = len(lst),len(lst)
            for i1 in range(l):
                if nn<lst[i1]:
                    ind = i1
                else:
                    pass
            if ind!=l: #arrangable
                nums[i-1], nums[i+ind] = nums[i+ind], nums[i-1]
                # Sort the descending array ascendingly 
                ln = len(nums)
                for i1 in range((ln-i)//2):
                    nums[i+i1], nums[ln-1-i1] = nums[ln-1-i1], nums[i+i1]
                
                return
            else:
                if i>=2:
                    nextPer(nums[i-1:],nums[i-2], i-1)
                else:
                    ln = len(nums)
                    for i in range(ln//2):
                        nums[i], nums[ln-1-i] = nums[ln-1-i], nums[i]
                    return
            return
        l = len(nums)
        nextPer(nums[l-1:], nums[l-2],l-1)
        return 