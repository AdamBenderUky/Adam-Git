# problem_10.py

def sieve_of_eratosthenes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit, start):
                sieve[multiple] = False
                
    return [num for num, is_prime in enumerate(sieve) if is_prime]

if __name__ == "__main__":
    limit = 2000000
    primes = sieve_of_eratosthenes(limit)
    result = sum(primes)
    print(f"The sum of all primes below {limit} is {result}")
