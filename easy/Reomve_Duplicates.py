class Solution:
    def remove_duplicates(self, nums):
        """
        Removes duplicates from a sorted array in-place and returns the modified array.

        Args:
            nums (List[int]): The input sorted array with possible duplicates.

        Returns:
            List[int]: The modified array with duplicates removed.

        """
        if not nums:
            return []

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return nums[:i+1]

s = Solution()
print(s.remove_duplicates([1, 1, 2]))
