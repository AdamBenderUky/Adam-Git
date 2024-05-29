# problem_13.py

def read_numbers(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def first_ten_digits_of_sum(numbers):
    total_sum = sum(numbers)
    return str(total_sum)[:10]

if __name__ == "__main__":
    filename = '../data/data_13.txt'
    numbers = read_numbers(filename)
    result = first_ten_digits_of_sum(numbers)
    print(f"The first ten digits of the sum of the numbers is {result}")
