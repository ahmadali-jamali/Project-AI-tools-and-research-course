#version first----
def matrix_multiply(a, b):
    
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    
    if cols_a != rows_b:
        raise ValueError("Number of columns in A must match rows in B")
    
    #   initialize result matrix
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result


# New optimized version
def matrix_multiply_optimized(a, b):
    
    return [
        [sum(a_row[k] * b[k][b_col] for k in range(len(a[0]))) 
        for b_col in range(len(b[0]))
    ] 
    for a_row in a
    ]

if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print("Naive:", matrix_multiply(a, b))
    print("Optimized:", matrix_multiply_optimized(a, b))