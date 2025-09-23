class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        temp=[[0 for i in range(0,len(matrix))] for j in range(0,len(matrix[0]))]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                temp[j][i]=matrix[i][j]
        return temp
        