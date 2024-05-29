# problem_11.py

def read_grid(filename):
    with open(filename, 'r') as file:
        grid = [list(map(int, line.split())) for line in file]
    return grid

def greatest_product(grid, length):
    rows = len(grid)
    cols = len(grid[0])
    max_product = 0
    max_numbers = []

    for row in range(rows):
        for col in range(cols):
            # Horizontal right
            if col + length <= cols:
                product = 1
                numbers = []
                for i in range(length):
                    product *= grid[row][col + i]
                    numbers.append(grid[row][col + i])
                if product > max_product:
                    max_product = product
                    max_numbers = numbers

            # Vertical down
            if row + length <= rows:
                product = 1
                numbers = []
                for i in range(length):
                    product *= grid[row + i][col]
                    numbers.append(grid[row + i][col])
                if product > max_product:
                    max_product = product
                    max_numbers = numbers

            # Diagonal down-right
            if col + length <= cols and row + length <= rows:
                product = 1
                numbers = []
                for i in range(length):
                    product *= grid[row + i][col + i]
                    numbers.append(grid[row + i][col + i])
                if product > max_product:
                    max_product = product
                    max_numbers = numbers

            # Diagonal down-left
            if col - length >= -1 and row + length <= rows:
                product = 1
                numbers = []
                for i in range(length):
                    product *= grid[row + i][col - i]
                    numbers.append(grid[row + i][col - i])
                if product > max_product:
                    max_product = product
                    max_numbers = numbers

    return max_product, max_numbers

if __name__ == "__main__":
    filename = '../data/data_11.txt'
    grid = read_grid(filename)
    length = 4
    result, numbers = greatest_product(grid, length)
    print(f"The greatest product of {length} adjacent numbers in the grid is {result}, from the numbers {numbers}")
