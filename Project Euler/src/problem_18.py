import os

def read_triangle(file_path):
    with open(file_path, 'r') as file:
        triangle = [[int(num) for num in line.split()] for line in file]
    return triangle

def max_path_sum(triangle):
    n = len(triangle)
    path = [[[] for _ in range(len(row))] for row in triangle]
    
    # Initialize the path for the bottom row
    for j in range(len(triangle[-1])):
        path[-1][j] = [(n-1, j)]
    
    # Start from the second last row and move upwards
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            if triangle[i + 1][j] > triangle[i + 1][j + 1]:
                triangle[i][j] += triangle[i + 1][j]
                path[i][j] = [(i, j)] + path[i + 1][j]
            else:
                triangle[i][j] += triangle[i + 1][j + 1]
                path[i][j] = [(i, j)] + path[i + 1][j + 1]
    
    max_path = path[0][0]
    max_sum = triangle[0][0]
    
    return max_sum, max_path

def display_path(triangle, path):
    n = len(triangle)
    path_set = set(path)
    for i in range(n):
        row = []
        for j in range(len(triangle[i])):
            if (i, j) in path_set:
                row.append(f"({triangle[i][j]})")
            else:
                row.append(f" {triangle[i][j]} ")
        print(" ".join(row))

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'triangle.txt')
    triangle = read_triangle(file_path)
    max_sum, max_path = max_path_sum(triangle)
    print("The maximum total from top to bottom is:", max_sum)
    print("The path taken is:", max_path)
    print("The triangle with the path highlighted:")
    display_path(triangle, max_path)
