class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        matrix2=[row[:] for row in matrix]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j]==0:
                    matrix2[i] = [0] * len(matrix[i])
                    temp=0
                    while temp<len(matrix):
                        matrix2[temp][j]=0
                        temp=temp+1
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                matrix[i][j]=matrix2[i][j]
        return matrix2
        
        