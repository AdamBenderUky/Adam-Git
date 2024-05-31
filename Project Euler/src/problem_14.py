# problem_14.py

def collatz_sequence_length(n, cache):
    original_n = n
    length = 0
    
    while n != 1:
        if n < len(cache) and cache[n] != 0:
            length += cache[n]
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    
    # Cache the result for the original number
    cache[original_n] = length
    return length

def find_longest_collatz_chain(limit):
    cache = [0] * (limit + 1)
    max_length = 0
    max_starting_number = 0
    
    for i in range(1, limit):
        length = collatz_sequence_length(i, cache)
        if length > max_length:
            max_length = length
            max_starting_number = i
    
    return max_starting_number, max_length

if __name__ == "__main__":
    limit = 1000000
    starting_number, max_length = find_longest_collatz_chain(limit)
    print(f"The starting number under {limit} that produces the longest chain is {starting_number}, with a chain length of {max_length}")
