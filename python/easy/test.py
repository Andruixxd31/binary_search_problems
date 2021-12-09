lass Solution:
    def solve(self, matrix):
        valid = True
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    valid = False
                    break
        return valid
