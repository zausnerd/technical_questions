matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

matrix2 = [
  [1,2],
  [2,2]
]

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        def isDiagIdentical(coord, rows, cols, matrix):
            row, col = coord
            if row >= rows or col >= cols:
                return True
            curr = matrix[row][col]
            while row < rows and col < cols:
                if matrix[row][col] != curr:
                    return False
                row += 1
                col += 1
            return True

        max_len = max(len(matrix), len(matrix[0]))
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(0, max_len):
            if not (isDiagIdentical((0, i), rows, cols, matrix) and 
                isDiagIdentical((i, 0), rows, cols, matrix)):
                return False
        return True
sol = Solution()

print(sol.isToeplitzMatrix(matrix)) # Expected: True
print(sol.isToeplitzMatrix(matrix2)) # Expected: False