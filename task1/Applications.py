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

import test