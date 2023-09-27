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

        dict = {}
        for i , n in enumerate(self.nums): 
            sub = self.target - n 
            if sub in dict:
                return dict[sub], i 
            
            dict[n] = i 

        return -1 
    

nums = [2,11,7,15]
target = 9

s = Solution(nums, target)
print(s.two_sum())