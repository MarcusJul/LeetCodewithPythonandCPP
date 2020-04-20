class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        
        def lrf():
            s,l,i = 1,len(nums),0
            while(i<l):
                s*=nums[i]
                i+=1
                yield s
                
        def rlf():
            s,l = 1,len(nums)
            i = l-1
            while(l>-1):
                s*=nums[i]
                i-=1
                yield s
            
        lrfunc = lrf()
        lr = [next(lrfunc) for i in range(l)]
        rlfunc = rlf()
        rl = [next(rlfunc) for i in range(l)]
        
        ret = [lr[i-1]*rl[l-2-i] for i in range(1,l-1)]
        
        return [rl[l-2]]+ret+[lr[l-2]]
            
        