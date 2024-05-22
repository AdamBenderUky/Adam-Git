# problem_7.py

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

def get_ordinal_suffix(n):
    if 10 <= n % 100 <= 20:
        return "th"
    else:
        suffixes = {1: "st", 2: "nd", 3: "rd"}
        return suffixes.get(n % 10, "th")

if __name__ == "__main__":
    n = 10001
    result = nth_prime(n)
    suffix = get_ordinal_suffix(n)
    print(f"The {n}{suffix} prime number is {result}")
