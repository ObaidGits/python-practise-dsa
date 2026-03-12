"""
Program: Print the first N prime numbers

Description:
A prime number is a number greater than 1 that has no divisors
other than 1 and itself.

This program reads an integer N from the user and generates the
first N prime numbers. It checks each number starting from 2 and
determines whether it is prime by testing divisibility up to the
square root of that number.

Input:
An integer N representing how many prime numbers to generate.

Output:
A list containing the first N prime numbers.
"""

# Read the number of prime numbers required
n = int(input("Enter the Value of N: "))

# List to store the prime numbers found
primes = []

# Counter to track how many prime numbers have been found
count = 0

# Number currently being checked for primality
num = 2

# Continue until we find n prime numbers
while count < n:

    # Assume the current number is prime
    is_prime = True

    # Check if num is divisible by any number from 2 to √num
    for j in range(2, int(num ** 0.5) + 1):

        # If divisible, num is not prime
        if num % j == 0:
            is_prime = False
            break

    # If no divisor was found, num is prime
    if is_prime:
        primes.append(num)   # Add the prime number to the list
        count += 1           # Increase the count of primes found

    # Move to the next number
    num += 1

# Print the list of first n prime numbers
print(primes)

# <--------------------------------------------- My Solution (NON Optimal) --------------------------------------------->
# n = int(input("Enter the Value of N"))
# primes = []
# i = 1
# curr_num = 2
# while i<=n:
#     facts = 0
#     for j in range(1, curr_num):
#         if curr_num%j == 0:
#             facts += 1
#     if facts < 2:
#         primes.append(curr_num)
#         i += 1
#     curr_num += 1
    
# print("Curr Num", curr_num)
# print("Primes", primes)