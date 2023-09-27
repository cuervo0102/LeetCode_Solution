class Solution :
    def __init__(self, nums, target):
        """
        Initialize the Solution class with a list of numbers and a target value.

        Args:
            nums (list[int]): A list of integers.
            target (int): The target value to find pairs that sum up to.

        Attributes:
            nums (list[int]): The list of integers.
            target (int): The target value.

        """
        
        self.nums = nums
        self.target = target 


    def two_sum(self) -> list:
        """
        Find pairs of numbers in the list that sum up to the target value.

        Returns:
            list of tuple: A list of tuples containing the indices of pairs that sum up to the target.

        """

        indices = []
        for i , n1 in enumerate(self.nums):
            for j , n2 in enumerate(self.nums[i+1:]):
                sum = n1 + n2 
                if sum == self.target:
                    indices.append((i , j+i+1))

        return indices
                
                
nums = [2,11,7,15]
target = 9

s = Solution(nums, target)
print(s.two_sum())

        