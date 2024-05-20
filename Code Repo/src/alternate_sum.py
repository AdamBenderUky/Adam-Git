def read_data(file_path):
    """Read numbers from a file and return them as a list of integers."""
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [int(line.strip()) for line in data]

def alternate_sum(numbers):
    """Calculate the alternating sum of a list of numbers (sum-subtract-sum-...)."""
    result = 0
    for i, number in enumerate(numbers):
        if i % 2 == 0:
            result += number
        else:
            result -= number
    return result

def main():
    data_file_path = '../data/data.txt'  # Adjust the path if necessary
    numbers = read_data(data_file_path)
    total = alternate_sum(numbers)
    print(f"The alternating sum of the numbers is: {total}")

if __name__ == "__main__":
    main()
