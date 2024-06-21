def sum_of_proper_divisors(n):
    proper_divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            proper_divisors_sum += i
            if i != n // i:
                proper_divisors_sum += n // i
    return proper_divisors_sum

def find_abundant_numbers(limit):
    abundant_numbers = []
    for i in range(12, limit + 1):
        if sum_of_proper_divisors(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers

def can_be_written_as_abundant_sum(limit, abundant_numbers):
    can_be_written = [False] * (limit + 1)
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            if abundant_numbers[i] + abundant_numbers[j] <= limit:
                can_be_written[abundant_numbers[i] + abundant_numbers[j]] = True
            else:
                break
    return can_be_written

def sum_of_non_abundant_sums(limit):
    abundant_numbers = find_abundant_numbers(limit)
    can_be_written = can_be_written_as_abundant_sum(limit, abundant_numbers)
    total_sum = 0
    for i in range(1, limit + 1):
        if not can_be_written[i]:
            total_sum += i
    return total_sum

if __name__ == "__main__":
    limit = 28123
    result = sum_of_non_abundant_sums(limit)
    print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is:", result)
