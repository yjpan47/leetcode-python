class Solution(object):
    
    def move_horizontal(self, matrix, row_n, start_col, end_col, step):
        result = []
        for c in range(start_col, end_col + step, step):
            value = matrix[row_n][c]
            result.append(value)
        return result

    def move_vertical(self, matrix, col_n, start_row, end_row, step):
        result = []
        for r in range(start_row, end_row + step, step):
            value = matrix[r][col_n]
            result.append(value)
        return result
    
    
    def spiralOrder(self, matrix):
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
            
        
        spiral = []
        
        i, j = 0, len(matrix) - 1
        m, n = 0, len(matrix[0]) - 1
        
        total = (j + 1) * (n + 1) 
        
        while True:
            spiral.extend(self.move_horizontal(matrix, i, m, n, 1))
            if len(spiral) >= total:
                break
            i += 1
            spiral.extend(self.move_vertical(matrix, n, i, j, 1))
            if len(spiral) >= total:
                break
            n -= 1
            spiral.extend(self.move_horizontal(matrix, j, n, m, -1))
            if len(spiral) >= total:
                break
            j -= 1
            spiral.extend(self.move_vertical(matrix, m, j, i, -1))
            if len(spiral) >= total:
                break
            m += 1
        
        return spiral