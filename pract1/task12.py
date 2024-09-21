def task12(matrix):

    if len(matrix) == 0 or len(matrix[0]==0):
        raise ValueError("Матрица не должна быть пустой")
    
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("Была введена не квадратная матрица")
        
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * task12(sub_matrix)
    
    return det

matrix = [[1, 2, 3],
          [0, 1, 4],
          [5, 6, 0]]

try:
    result = task12(matrix)
    print(f"Определитель матрицы: {result}")
except ValueError as e:
    print(f"Ошибка: {e}")