class Solution:
    def selectionSort(self, arr):
        """
        Sorts a list of numbers in ascending order using a simple
        selection-style sorting approach.

        The algorithm iterates through the list and compares each element
        with the remaining elements. If a smaller element is found, the
        values are swapped. This gradually moves smaller elements toward
        the beginning of the list.

        Args:
            arr (list[int]): List of integers to be sorted.

        Time Complexity:
            O(n^2)

        Space Complexity:
            O(1) – sorting is done in-place.
        """
        temp = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp


# take input
arr = list(map(int, input("Enter numbers separated by space: ").split()))

# create object and call function
obj = Solution()
obj.selectionSort(arr)

# print sorted array
print("Sorted array:", arr)