# problem_21.py

def sum_of_proper_divisors(n):
    proper_divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            proper_divisors_sum += i
            if i != n // i:
                proper_divisors_sum += n // i
    return proper_divisors_sum

def find_amicable_numbers(limit):
    amicable_numbers = set()
    amicable_pairs = []
    for a in range(2, limit):
        b = sum_of_proper_divisors(a)
        if b != a and b < limit and sum_of_proper_divisors(b) == a:
            if (a, b) not in amicable_pairs and (b, a) not in amicable_pairs:
                amicable_pairs.append((a, b))
                amicable_numbers.add(a)
                amicable_numbers.add(b)
    return amicable_numbers, amicable_pairs

if __name__ == "__main__":
    limit = int(input("Enter the limit to find amicable numbers: "))
    amicable_numbers, amicable_pairs = find_amicable_numbers(limit)
    result = sum(amicable_numbers)
    print("The sum of all the amicable numbers under", limit, "is:", result)
    print("The amicable pairs are:")
    for pair in amicable_pairs:
        print(pair)
