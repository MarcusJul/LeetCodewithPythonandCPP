class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        if l==1:
            return matrix
        temp = [[0]*l for i in range(l)]
        
        for i in range(l):
            for j in range(l):
                temp[i][j] = matrix[l-j-1][i]
        print(temp)
        for i in range(l):
            for j in range(l):
                matrix[i][j] = temp[i][j]