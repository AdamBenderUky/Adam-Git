def find_fibonacci_index_with_digits(target_digits):
    a, b = 1, 1
    index = 2
    while len(str(b)) < target_digits:
        a, b = b, a + b
        index += 1
    return index

if __name__ == "__main__":
    target_digits = 1000
    result = find_fibonacci_index_with_digits(target_digits)
    print("The index of the first term in the Fibonacci sequence to contain", target_digits, "digits is:", result)