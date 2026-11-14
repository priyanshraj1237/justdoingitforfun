class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)-1
        columns=len(matrix[0])-1
        i ,j=0,0
        while(i<= row and j<=columns):
            if matrix[i][j]==target:
                return True
            if matrix[i][columns]>=target :
                j+=1
            if matrix[i][columns]<target :
                i+=1
        return False