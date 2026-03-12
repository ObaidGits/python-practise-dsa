"""
File: string_series_transform.py

Problem:
Read three strings from STDIN (each on a new line) and perform the following
transformations:

1. In the first string, replace all vowels with '$'.
2. In the second string, replace all consonants with '#'.
3. In the third string, convert uppercase letters to lowercase and
   lowercase letters to uppercase.

Finally, print the three transformed strings in a single line separated by spaces.

Example:
Input:
Hello
Hi
Good Morning

Output:
H$ll$ #i gOOD mORNING
"""

# Read three input strings
str1 = input()
str2 = input()
str3 = input()

# Initialize empty strings to store results
new_str1 = ""
new_str2 = ""
new_str3 = ""

# Define vowels for checking
vowels = "aeiouAEIOU"

# Replace vowels with '$' in the first string
for s in str1:
    if s in vowels:
        new_str1 += "$"
    else:
        new_str1 += s

# Replace consonants with '#' in the second string
for s in str2:
    if s.isalpha() and s not in vowels:
        new_str2 += "#"
    else:
        new_str2 += s

# Swap case in the third string
for s in str3:
    if s.isupper():
        new_str3 += s.lower()
    else:
        new_str3 += s.upper()

# Print the transformed strings in a single line
print(new_str1 + " " + new_str2 + " " + new_str3)