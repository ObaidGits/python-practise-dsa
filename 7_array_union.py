class Solution:
    def findUnion(self, a, b):
        """
        Compute the union of two arrays.

        This function combines the elements of two input lists, removes
        duplicates using a set, and returns a sorted list containing the
        unique elements from both arrays.

        Args:
            a (list): First list of integers.
            b (list): Second list of integers.

        Returns:
            list: A sorted list containing the unique elements
                  from both input lists.
        """
        # code here
        new_list = a + b
        new_set = set(new_list)
        new_list = list(new_set)
        new_list.sort()

        return list(new_list)


if __name__ == "__main__":
    """
    Example input format:
    Enter elements of first array separated by space: 1 2 3 4
    Enter elements of second array separated by space: 3 4 5 6
    """

    a = list(map(int, input("Enter elements of first array separated by space: ").split()))
    b = list(map(int, input("Enter elements of second array separated by space: ").split()))

    sol = Solution()
    result = sol.findUnion(a, b)

    print("Union:", result)