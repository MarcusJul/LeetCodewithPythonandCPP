class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binary(left, right, tar):
            if numbers[left]==tar:
                return left
            if numbers[right]==tar:
                return right
            if right-left==1 or right==left:
                return None
            
            mid = int((left+right)/2)
            if numbers[mid]<tar:
                return binary(mid, right, tar)
            else:
                return binary(left, mid, tar)
        
        
        def findTar(ind):
            tar = target-numbers[ind]
            if tar>numbers[ind]:
                ret = binary(ind+1,len(numbers)-1,tar)        
            elif tar==numbers[ind]:
                try:
                    left = numbers[ind-1]
                    if left==tar:
                        return [ind,ind+1]
                    else:
                        return [ind+1,ind+2]
                except:
                    right = numbers[ind+1]
                    return [ind+1, ind+1+1]
            else:
                ret = binary(0, ind-1, tar)
            if ret==None:
                return []
            else:
                print(ret,numbers[ind])
                return [ret+1,ind+1] if numbers[ret]<numbers[ind] else [ind+1, ret+1]
        
        for i in range(len(numbers)-1):
            ret = findTar(i)
            if ret==[]:
                pass
            else:
                return ret