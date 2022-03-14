class Solution:
    def solve(self, matrix):
        n = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    self.cn(matrix,i,j) 
                    n+=1
        return n

    def cn(self,matrix, i, j):
        matrix[i][j] = 0
        if i > 0:
            if matrix[i-1][j] == 1: self.cn(matrix, i-1,j)
        if i < len(matrix) - 1:
            if matrix[i+1][j] == 1: self.cn(matrix, i+1,j) 
        if j > 0:
            if matrix[i][j-1] == 1: self.cn(matrix, i,j-1)

        if j < len(matrix[0]) - 1:
            if matrix[i][j+1] == 1: self.cn(matrix, i,j+1)
