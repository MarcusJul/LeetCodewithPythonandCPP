class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        lpl = n #how many left parenthesis you have
        mod = ''
        val = 0 #the total value of the whole mod
        def traverse(lpl, 
                     val, 
                     ret, 
                     mod #mod should be the current
                    ):
            if val==0:
                if lpl>0:
                    return traverse(lpl-1, val+1, ret, mod+'(')
                else:
                    ret.append(mod)# the val is 0 and you have used up all lp
                    return ret
            else: #lp in place is more than rp
                if lpl>0:
                    ret = traverse(lpl-1, val+1, ret, mod+'(') # start with left
                    return traverse(lpl, val-1, ret, mod+')') # start with right
                else:# no lp left, add a rp
                    return traverse(lpl, val-1, ret, mod+')')
                    
                    
        return traverse(lpl,0,[],'')