"""
Find the element that appears only once in an array where every other element appears exactly twice.

Two approaches are demonstrated:

1. Optimal Approach (Bit Manipulation using XOR)
   - XOR has useful properties:
        a ^ a = 0
        a ^ 0 = a
   - When XOR is applied across all numbers, duplicate numbers cancel out,
     leaving only the single number.

   Time Complexity : O(n)
   Space Complexity: O(1)

2. Non-Optimal Approach (Hash Map / Dictionary)
   - Count frequency of each element using a dictionary.
   - Return the element whose frequency is 1.

   Time Complexity : O(n)
   Space Complexity: O(n)

Sample Input:
4 1 2 1 2

Sample Output:
Single Number (Optimal)     : 4
Single Number (Non-Optimal) : 4
"""

from typing import List


class Solution:

    def singleNumber_optimal(self, nums: List[int]) -> int:
        """
        Optimal solution using XOR.

        Args:
            nums (List[int]): List of integers where every number appears
                              twice except one.

        Returns:
            int: The number that appears only once.
        """
        result = 0
        for num in nums:
            result ^= num
        return result


    def singleNumber_non_optimal(self, nums: List[int]) -> int:
        """
        Non-optimal solution using a dictionary to count frequencies.

        Args:
            nums (List[int]): List of integers where every number appears
                              twice except one.

        Returns:
            int: The number that appears only once.
        """
        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        for key, value in my_dict.items():
            if value == 1:
                return key


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))

    sol = Solution()

    print("Single Number (Optimal)     :", sol.singleNumber_optimal(nums))
    print("Single Number (Non-Optimal) :", sol.singleNumber_non_optimal(nums))