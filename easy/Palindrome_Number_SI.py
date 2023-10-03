#FaceBook
class Solution:
    def __init__(self, num):
        """
        Initialize the Solution class with an integer.

        Args:
            num (int): The integer to check for palindrome.

        Attributes:
            num (int): The integer to be checked.

        """

        self.num = num

    def check_palindrome(self) -> bool:
        """
        Check if the integer is a palindrome.

        Returns:
            bool: True if the integer is a palindrome, False otherwise.

        """

        num_str = str(self.num)  
        middle = len(num_str) // 2
        left = num_str[:middle]
        right = num_str[middle:]

        for i in range(middle):
            if left[i] != right[-1]:
                return False

        return True


s = Solution(212)

print(s.check_palindrome())  # Output: True (121 is a palindrome)

