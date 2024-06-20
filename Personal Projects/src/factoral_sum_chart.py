import math
import matplotlib.pyplot as plt
import csv
import os

def sum_of_factorial_digits(number):
    # Calculate the factorial of the given number
    fact = math.factorial(number)

    # Convert the factorial result to a string, then to a list of digits
    digits = [int(digit) for digit in str(fact)]

    # Sum the digits
    sum_of_digits = sum(digits)

    return sum_of_digits

def save_data_to_csv(x_values, y_values, filename='factorial_digit_sum_data.csv'):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Number', 'Sum of Digits of Factorial'])
        csv_writer.writerows(zip(x_values, y_values))

# Generate data for the chart
x_values = list(range(1, 901))
y_values = [sum_of_factorial_digits(x) for x in x_values]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.xlabel('Number')
plt.ylabel('Sum of Digits of Factorial')
plt.title('Sum of Digits of Factorial for Numbers 1 to 100')
plt.grid(True)
plt.show()

# Save data to CSV in the same directory as the script
save_data_to_csv(x_values, y_values)

# Print the absolute path of the saved CSV file
print(f"CSV file saved to {os.path.abspath('factorial_digit_sum_data.csv')}")
