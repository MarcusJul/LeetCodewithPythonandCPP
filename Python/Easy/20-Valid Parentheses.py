class Solution:
    def isValid(self, s: str) -> bool:
        if s=='':
            return True
        if len(s)==1:
            return False
        d = {'(':')','{':'}','[':']'}
        dr = [')',']','}']
                
        def recCheck(ind):
            
            
            return 
        
        
        def StackCheck(ind, stack):
            if s[ind] in d:
                if ind+1<=len(s)-1:
                    stack.append(s[ind])
                    return StackCheck(ind+1,stack)
                else:
                    return False
            else:
                if stack==[]:
                    return False
                left = stack[-1]
                stack = stack[:-1]
                if s[ind]==d[left]:
                    if ind+1<=len(s)-1:
                        return StackCheck(ind+1,stack)
                    else:
                        if stack!=[]:
                            return False
                        else:
                            return True
                else:
                    return False
        return StackCheck(0, [])
    