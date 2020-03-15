class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums==[]:
            return [[]]
        if len(nums)==1:
            return [nums]
        def per(lst1, lst2, tlst):
            if len(lst2)==2:
                tlst += [lst1+lst2,lst1+[lst2[1],lst2[0]]]
                return tlst
            else:
                for i in range(len(lst2)):
                    t_lst = per(lst1+[lst2[i]],lst2[:i]+lst2[i+1:],tlst)
            return tlst
        
        return per([],nums,[])