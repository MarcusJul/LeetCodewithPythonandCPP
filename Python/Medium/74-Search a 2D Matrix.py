class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Find the row
        if matrix==[[]]:
            return False
        m = len(matrix)
        if m==0:
            return False
        n = len(matrix[0])
        
        if matrix[m-1][n-1]<target:
            return False
        if matrix[0][0]>target:
            return False
        
        left, right = 0, m-1
        while(left<=right):
            mid = (left+right)//2
            if matrix[mid][0]<=target:
                if matrix[mid][n-1] >= target:
                    break
                else:
                    left = mid+1
            else:
                right = mid-1
            # print(left, right, mid)
        # print(mid)
        
        
        def binSearch(r, tar):
            row = matrix[r]
            if row[n-1]==tar:
                return True
            elif row[n-1]<tar:
                return False
            else:
                pass
            
            left, right = 0, n-1
            while(left<=right):
                mid = (left+right)//2
                if row[mid]==tar:
                    return True
                else:
                    if row[mid]<tar:
                        left = mid+1
                    else:
                        right = mid-1
                # print(left, right, mid)
            return False
        
        if n!=1:
            res = binSearch(mid, target)
        else:
            res = matrix[mid][0]==target
        
        return res 

# solution 2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix==[[]]:
            return False
        m = len(matrix)
        if m==0:
            return False
        n = len(matrix[0])
        
        if matrix[m-1][n-1]<target:
            return False
        if matrix[0][0]>target:
            return False
        
        left, right = 0, n*m-1
        
        def getRowCol(mid):
            row, col = mid//n, mid%n 
            return row, col
        
        while(left<=right):
            mid = (left+right)//2
            row, col = getRowCol(mid)
            if matrix[row][col]==target:
                return True
            else:
                if matrix[row][col]<target:
                    left = mid+1
                else:
                    right = mid-1
                
        return False