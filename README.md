# Project Euler Solutions

Welcome to my Project Euler solutions repository! Here, you'll find my solutions to various Project Euler problems implemented in Python.

## About Project Euler

Project Euler is a series of challenging mathematical/computer programming problems that require more than just mathematical insights to solve. Aimed at those who enjoy problem-solving and computational exploration, it features problems in a wide range of categories including number theory, combinatorics, and graph theory.

## Prerequisites

To run these solutions, you'll need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

## Setup Instructions

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/yourusername/ProjectEuler.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ProjectEuler
    ```
3. Ensure you have the necessary dependencies installed. You can set up a virtual environment and install any required packages:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt  # If there is a requirements file
    ```

## Solved Problems

### Problem 1: Multiples of 3 or 5
- **Description:** Find the sum of all the multiples of 3 or 5 below 1000.
- **Solution:** [problem_1.py](src/problem_1.py)

### Problem 2: Even Fibonacci Numbers
- **Description:** Find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.
- **Solution:** [problem_2.py](src/problem_2.py)

### Problem 3: Largest Prime Factor
- **Description:** Find the largest prime factor of the number 600851475143.
- **Solution:** [problem_3.py](src/problem_3.py)

## Running the Solutions

To run a solution, navigate to the `src` folder and execute the corresponding Python file. For example, to run the solution for Problem 1:

```sh
cd src
python problem_1.py