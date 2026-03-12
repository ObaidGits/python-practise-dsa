class Solution:
    def longestSubarray(self, arr, k):
        """
        Returns the length of the longest subarray
        whose sum equals k and the subarray itself.

        Uses prefix sum with a hashmap to handle
        both positive and negative numbers.

        Args:
            arr (list): List of integers
            k (int): Target sum

        Returns:
            tuple: (length_of_subarray, subarray)
        """

        prefix_sum = 0
        longest = 0
        seen = {}

        start_index = -1
        end_index = -1

        for i in range(len(arr)):

            prefix_sum += arr[i]

            # case 1: subarray from start
            if prefix_sum == k:
                longest = i + 1
                start_index = 0
                end_index = i

            # case 2: subarray in middle
            if (prefix_sum - k) in seen:
                length = i - seen[prefix_sum - k]

                if length > longest:
                    longest = length
                    start_index = seen[prefix_sum - k] + 1
                    end_index = i

            # store first occurrence
            if prefix_sum not in seen:
                seen[prefix_sum] = i

        subarray = arr[start_index:end_index+1] if longest > 0 else []

        return longest, subarray


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    sol = Solution()
    length, subarray = sol.longestSubarray(arr, k)

    print(length)
    print(subarray)