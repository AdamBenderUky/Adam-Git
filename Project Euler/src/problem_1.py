# problem_1.py

def sum_of_multiples(limit):
    total_sum = 0
    for number in range(limit):
        if number % 3 == 0 or number % 5 == 0:
            total_sum += number
    return total_sum

if __name__ == "__main__":
    limit = 1000
    result = sum_of_multiples(limit)
    print(f"The sum of all multiples of 3 or 5 below {limit} is {result}")