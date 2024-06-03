# problem_16.py

def sum_of_digits_of_power(base, exponent):
    number = base ** exponent
    string_number = str(number)
    list_of_numbers = [int(char) for char in string_number]
    return sum(list_of_numbers)

if __name__ == "__main__":
    base = 2
    exponent = 1000
    result = sum_of_digits_of_power(base, exponent)
    print(f"The sum of the digits of {base}^{exponent} is {result}")
