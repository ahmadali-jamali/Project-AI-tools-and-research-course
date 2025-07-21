import time
from matrix import matrix_multiply, matrix_multiply_optimized  # Option A
# from matrix_optimized import matrix_multiply_optimized  # Option B

def generate_matrix(size):
    return [[i + j for j in range(size)] for i in range(size)]

def test_performance():
    sizes = [10, 50, 100]
    for size in sizes:
        a = generate_matrix(size)
        b = generate_matrix(size)
        
        # Test naive version
        start = time.time()
        matrix_multiply(a, b)
        naive_time = time.time() - start
        
        # Test optimized version
        start = time.time()
        matrix_multiply_optimized(a, b)
        optimized_time = time.time() - start
        
        print(f"Size {size}x{size}: Naive={naive_time:.4f}s | Optimized={optimized_time:.4f}s")

if __name__ == "__main__":
    test_performance()