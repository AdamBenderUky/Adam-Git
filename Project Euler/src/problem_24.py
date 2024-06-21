import math

def find_millionth_permutation(digits, position):
    permutation = []
    k = position - 1  # Adjust for zero indexing
    available_digits = digits[:]

    for i in range(len(digits), 0, -1):
        factorial = math.factorial(i - 1)
        index = k // factorial
        permutation.append(available_digits.pop(index))
        k %= factorial

    return ''.join(map(str, permutation))

if __name__ == "__main__":
    digits = list(range(10))
    position = 1000000
    result = find_millionth_permutation(digits, position)
    print("The millionth lexicographic permutation of the digits 0 to 9 is:", result)