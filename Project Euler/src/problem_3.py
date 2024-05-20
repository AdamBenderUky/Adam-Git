# problem_3.py

def largest_prime_factor(n):
    # Initialize the smallest factor
    i = 2
    # Divide n by i until i^2 exceeds n
    while i * i <= n:
        # If i divides n, divide n by i
        if n % i == 0:
            n //= i
        else:
            # Increment i if it doesn't divide n
            i += 1
    # Return the remaining n which is the largest prime factor
    return n

if __name__ == "__main__":
    number = 6008514751432
    result = largest_prime_factor(number)
    print(f"The largest prime factor of {number} is {result}")