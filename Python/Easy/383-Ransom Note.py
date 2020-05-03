class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        left, right = {}, {}
        
        if len(ransomNote)>len(magazine):
            return False
        
        for char in ransomNote:
            try:
                left[char] += 1
            except:
                left[char] = 1
        
        for char in magazine:
            try:
                right[char] += 1
            except:
                right[char] = 1
        
        

        
        for k,v in left.items():
            if k not in right:
                return False
            else:
                if left[k] > right[k]:
                    return False
        
        
        return True