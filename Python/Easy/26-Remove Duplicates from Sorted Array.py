class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = dict().fromkeys(nums,0)
        nums[:len(d)] = sorted(d)
        return len(d)