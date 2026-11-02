class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        one = 0
        two = 0

        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    one += mat[i][j]

                elif i + j == len(mat) - 1 and i != j:
                    two += mat[i][j]
            
        return one + two

        

        