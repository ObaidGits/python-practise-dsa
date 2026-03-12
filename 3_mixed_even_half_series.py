"""
Consider the following series:
0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8

This series is a mixture of two series:
• All the odd terms form even numbers in ascending order.
• Every even term is derived from the previous term using the formula (x/2).

Write a program to find the nth term in this series.

Input:
The value n is a positive integer that should be read from STDIN.

Output:
The nth term calculated by the program should be written to STDOUT.
Other than the value of the nth term, no other characters, strings, or
messages should be written to STDOUT.

Example:
If n = 10, the 10th term in the series is derived from the 9th term.
The 9th term is 8, so the 10th term is (8/2) = 4.
Only the value 4 should be printed to STDOUT.

Constraint:
You can assume that n will not exceed 20,000.
"""

n = int(input())

if n % 2 == 0:
    print((n - 2) // 2)
else:
    print(n - 1)