class Solution:
    def search(self, arr, x):
        """
        Perform a linear search on the given list.

        This function iterates through the array and returns the index
        of the first occurrence of the target value `x`. If the element
        is not found in the array, the function returns -1.

        Args:
            arr (list): List of elements to search in.
            x (int/float/str): Target element to search for.

        Returns:
            int: Index of the first occurrence of `x` in `arr`,
                 or -1 if `x` is not present.
        """
        for index, num in enumerate(arr):
            if num == x:
                return index

        return -1


if __name__ == "__main__":
    # Take array input
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    
    # Take element to search
    x = int(input("Enter element to search: "))

    sol = Solution()
    result = sol.search(arr, x)

    print(result)