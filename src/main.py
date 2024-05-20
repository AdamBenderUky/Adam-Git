def read_data(file_path):
    """Read numbers from a file and return them as a list of integers."""
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [int(line.strip()) for line in data]

def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)

def main():
    data_file_path = '../data/data.txt'  # Adjust the path if necessary
    numbers = read_data(data_file_path)
    total = calculate_sum(numbers)
    print(f"The sum of the numbers is: {total}")

if __name__ == "__main__":
    main()