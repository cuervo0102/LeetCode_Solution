class Solution:
    def monotonic_array(self, nums):
        """
        Check if the given array is monotonic (either increasing or decreasing).

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            bool: True if the array is monotonic, False otherwise.
        """
        increasing = decreasing = True
        for i in range(len(nums) - 1):
            j = i + 1
            if nums[i] > nums[j]:
                increasing = False
            if nums[i] < nums[j]:
                decreasing = False

        return increasing or decreasing

s = Solution()
print(s.monotonic_array([1, 3, 2]))
