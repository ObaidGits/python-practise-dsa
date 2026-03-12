"""
Consider the series:
1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, ...

This series is a mixture of two sequences:
• All the odd-positioned terms form a Fibonacci series.
• All the even-positioned terms are prime numbers in ascending order.

Task:
Write a program to find the Nth term in this series.

Input:
A positive integer N is read from STDIN.

Output:
Print only the Nth term of the series to STDOUT.
No additional text or messages should be printed.

Example:
Input:
16

Output:
17
"""

# Read the input value
n = int(input())

# If N is even → find the (n/2)th prime number
if n % 2 == 0:
    k = n // 2          # Position in the prime number sequence
    count = 0           # Counts how many primes have been found
    num = 2             # Start checking from the first prime number

    while True:
        # Check if 'num' is prime
        for i in range(2, num):
            if num % i == 0:   # If divisible, it's not prime
                break
        else:
            # If loop completes without break → number is prime
            count += 1
            if count == k:     # If kth prime is reached
                print(num)
                break

        num += 1               # Check next number


# If N is odd → find the ((n+1)/2)th Fibonacci number
else:
    k = (n + 1) // 2           # Position in Fibonacci sequence
    a, b = 1, 1                # First two Fibonacci numbers

    # First two Fibonacci numbers are both 1
    if k <= 2:
        print(1)
    else:
        # Generate Fibonacci sequence up to kth term
        for _ in range(k - 2):
            a, b = b, a + b

        print(b)

# <--------------------------------------------- My Solution (NON Optimal) --------------------------------------------->
# n = int(input("Enter the Nth Number : "))
# if n%2 ==0:
#     #Print prime if n is Even
#     num_of_primes = n//2
#     primes = []
#     i = 1
#     curr_num = 2
#     while i<=num_of_primes:
#         facts = 0
#         for j in range(1, curr_num):
#             if curr_num%j == 0:
#                 facts += 1
#         if facts < 2:
#             primes.append(curr_num)
#             i += 1
#         curr_num += 1
#     print(primes[len(primes)-1])
# else:
#     #Print fib if n is Odd
#     num_of_fib = (n+1) // 2
#     temp = 0
#     num1 = 1
#     num2 = 1
#     fibs = [1, 1]
#     if num_of_fib >2:
#         for i in range(1, num_of_fib - 1):
#             fibs.append(num1+num2)
#             temp = num2
#             num2 = num1+num2
#             num1 = temp
#         print(fibs[len(fibs) - 1])