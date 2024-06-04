import os

def read_triangle(file_path):
    with open(file_path, 'r') as file:
        triangle = [[int(num) for num in line.split()] for line in file]
    return triangle

def max_path_sum(triangle):
    n = len(triangle)
    # Start from the second last row and move upwards
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Update the value to the sum of the current value and the max of the two adjacent values in the row below
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    # The top element will have the maximum sum
    return triangle[0][0]

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'triangle_67.txt')
    triangle = read_triangle(file_path)
    result = max_path_sum(triangle)
    print("The maximum total from top to bottom is:", result)
