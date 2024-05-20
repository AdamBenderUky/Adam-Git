# problem_2.py

def sum_even_fibonacci(limit):
    a, b = 1, 2
    total_sum = 0
    while a <= limit:
        if a % 2 == 0:
            total_sum += a
        a, b = b, a + b
    return total_sum

if __name__ == "__main__":
    limit = 4000000
    result = sum_even_fibonacci(limit)
    print(f"The sum of even-valued terms in the Fibonacci sequence whose values do not exceed {limit} is {result}")