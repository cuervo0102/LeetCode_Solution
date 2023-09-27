class Solution : 
    def __init__(self, num):
        self.num = num 


    def palindrome_number(self):

        if self.num < 0 : return False
        div = 1
        while self.num > 10 * div : 
            div *= 10

        while self.num:
            right = self.num % 10
            left = self.num // div

            if right != left : return False

            self.num = (self.num % div) // 10
            div = div / 100

        return True
    

s = Solution(121)
print(s.palindrome_number())
