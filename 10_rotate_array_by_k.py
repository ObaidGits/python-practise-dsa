"""
Rotate an array to the right by k steps.

This script demonstrates two approaches:

1. Optimal Approach (O(n) time, O(1) space)
   Uses the reversal technique:
   - Reverse the entire array
   - Reverse the first k elements
   - Reverse the remaining n-k elements

2. Non-Optimal Approach (O(n * k) time, O(1) space)
   Rotates the array one step at a time, repeated k times.

Sample Input:
1 2 3 4 5 6 7
3

Expected Output:
Optimal Rotation  : [5, 6, 7, 1, 2, 3, 4]
Non-Optimal Result: [5, 6, 7, 1, 2, 3, 4]
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Optimal rotation using the three-reversal method.

        Args:
            nums (List[int]): List of integers to rotate.
            k (int): Number of right rotations.

        Returns:
            None (modifies the list in-place)
        """
        n = len(nums)
        k = k % n

        def reverse(l: int, r: int):
            """
            Reverse elements in nums between indices l and r inclusive.
            """
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

    def rotate_non_optimal(self, nums: List[int], k: int) -> None:
        """
        Non-optimal rotation method.

        Rotates the array one step to the right repeatedly k times.
        Time Complexity: O(n * k)

        Args:
            nums (List[int]): List of integers to rotate.
            k (int): Number of rotations.

        Returns:
            None (modifies the list in-place)
        """
        n = len(nums)
        k = k % n
        arr = nums
        temp = 0

        for i in range(k):
            temp = arr[n - 1]
            for j in range(n - 1, 0, -1):
                arr[j] = arr[j - 1]
            arr[0] = temp


if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter rotation count k: "))

    # Optimal
    nums_opt = nums.copy()
    sol = Solution()
    sol.rotate(nums_opt, k)
    print("Optimal Rotation  :", nums_opt)

    # Non-optimal
    nums_non = nums.copy()
    sol.rotate_non_optimal(nums_non, k)
    print("Non-Optimal Result:", nums_non)