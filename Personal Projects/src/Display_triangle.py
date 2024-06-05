import pandas as pd
import matplotlib.pyplot as plt

# Specify the full path to the CSV file
file_path = r"C:\Users\ambe335\GitHubAdam\Adam-Git\Personal Projects\data\path.csv"

# Read the file line by line
with open(file_path, 'r') as file:
    lines = file.readlines()

# Parse the data into a triangle format
triangle = []
for line in lines:
    row = []
    for item in line.strip().split(','):
        if item.startswith('(') and item.endswith(')'):
            row.append((float(item[1:-1]), True))  # Mark path numbers
        else:
            row.append((float(item), False))
    triangle.append(row)

# Find the maximum row length for formatting
max_row_length = max(len(row) for row in triangle)
num_rows = len(triangle)

# Calculate dynamic font size
base_font_size = 10
dynamic_font_size = max(base_font_size - num_rows // 10, 5)

# Visualization
def plot_triangle_with_path(triangle, font_size):
    fig, ax = plt.subplots()

    # Create coordinates for the numbers
    y_offset = 0
    for row in triangle:
        x_offset = -len(row) / 2  # Adjust x_offset to center the row
        for num, is_path in row:
            color = 'red' if is_path else 'black'
            ax.text(x_offset, y_offset, f"{num:.2f}", color=color, ha='center', va='center', fontsize=font_size)
            x_offset += 1
        y_offset -= 1

    # Set limits to ensure all text is visible
    ax.set_xlim(-max_row_length / 2, max_row_length / 2)
    ax.set_ylim(-len(triangle), 1)

    # Hide axes
    ax.set_axis_off()
    plt.show()

# Plot the triangle with the path highlighted
plot_triangle_with_path(triangle, dynamic_font_size)
