class Solution:
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ref_dict = dict()
        for i in range(len(nums)):
            if nums[i] in ref_dict:
                ref_dict[nums[i]].append(i)
            else:
                ref_dict[nums[i]]=[i]
                
        for k in ref_dict.keys():
            if target-k!=k:
                if target-k in ref_dict.keys():
                    return sorted([ref_dict[k][0],ref_dict[target-k][0]]) 
            else:
                if len(ref_dict[k])>1:
                    return sorted(ref_dict[k])[0:2] 