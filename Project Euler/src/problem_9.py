# problem_9.py

def find_pythagorean_triplet(sum_total):
    for a in range(1, sum_total // 3):
        for b in range(a + 1, sum_total // 2):
            c = sum_total - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
    return None

if __name__ == "__main__":
    sum_total = 1000
    triplet = find_pythagorean_triplet(sum_total)
    if triplet:
        a, b, c = triplet
        product = a * b * c
        print(f"The Pythagorean triplet for which a + b + c = {sum_total} is {a}, {b}, {c}.")
        print(f"The product abc is {product}.")
    else:
        print(f"No Pythagorean triplet found for which a + b + c = {sum_total}.")
