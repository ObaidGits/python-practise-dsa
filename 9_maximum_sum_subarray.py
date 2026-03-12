"""
Compute the maximum sum of a strictly ascending contiguous subarray.

An ascending subarray is a sequence where each element is strictly
greater than the previous element. The algorithm scans the list once
and keeps track of the current ascending segment sum and the maximum
sum found so far.

Input:
- First line: space-separated integers representing the array.

Output:
- Prints the maximum ascending subarray sum.
"""

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        num_sum = nums[0]

        if len(nums) < 2:
            return nums[0]

        l, r = 0, 1

        while r < len(nums):

            if nums[r] > nums[r-1]:
                num_sum += nums[r]
            else:
                max_sum = max(max_sum, num_sum)
                l = r
                num_sum = nums[r]

            max_sum = max(max_sum, num_sum)
            r += 1

        return max_sum


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    sol = Solution()
    print(sol.maxAscendingSum(nums))