# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 21:30:37 2025

@author: chipp
"""
"""
This module provides a function to calculate the Greatest Common Divisor (GCD)
of two integers using the iterative Euclidean Algorithm, without relying on
Python's built-in 'math' module.
"""
#initial function
def calculate_gcd_euclidean(a, b):
    """
   Calculates the Greatest Common Divisor (GCD) of two integers using the
   Euclidean Algorithm

   Args:
       a (int): The first integer.
       b (int): The second integer.

   Returns:
       int: The GCD of a and b.
   """
 
    # 1. Take absolute values to handle negative inputs correctly.
    current_a = abs(a)
    current_b = abs(b)

    # Handle edge case where both inputs are zero.
    if current_a == 0 and current_b == 0:
        return 0

    # Ensure current_a is the larger number to start the standard procedure,
    if current_b > current_a:
        current_a, current_b = current_b, current_a

    # 2. Start the iterative process: loop continues as long as the remainder (current_b) is not zero.
    while current_b != 0:
        # 3. Calculate the remainder (r) when 'current_a' is divided by 'current_b'.
        remainder = current_a % current_b

        # 4. The old divisor (current_b) becomes the new dividend (current_a).
        current_a = current_b

        # 5. The remainder becomes the new divisor (current_b).
        current_b = remainder

    # 6. When the loop terminates (current_b is 0), current_a holds the GCD.
    return current_a

def get_valid_integer(prompt):
    """
    Prompts the user for input and validates that it is a valid integer.
    

    Args:
        prompt (str): The text to display to the user.

    Returns:
        int: A valid integer entered by the user.
    """
    while True:
        user_input = input(prompt)
        try:
            # Attempt to convert the string input to an integer.
            # This implicitly checks for valid characters.
            value = int(user_input)
            return value
        except ValueError:
            # Catch the error if the input is not a valid integer
            print(f"Error: '{user_input}' is invalid. Please enter a whole number (integer).")

if __name__ == "__main__":
    print("--- Euclidean Algorithm GCD Calculator ---")
    print("This program calculates the Greatest Common Divisor (GCD) of two integers.")
    print("Please enter your numbers below.\n")

   # 1. Accept user input
   # The algorithm accepts negatives (handled by abs() logic) and zero.
    number_1 = get_valid_integer("Enter the first integer: ")
    number_2 = get_valid_integer("Enter the second integer: ")

    # 2. Implement the Euclidean Algorithm using the inputs
    gcd_result = calculate_gcd_euclidean(number_1, number_2)

    # 3. Display the final result
    print(f"\nThe Greatest Common Divisor (GCD) of {number_1} and {number_2} is: {gcd_result}")