class Solution :
    """
    Initialize the solution class 
    Args : 
    Attributes : 

    """
    def are_pair(self, open , close):
        """
        Check if the given open and close characters form a valid pair.

        Args:
            open (str): The open character.
            close (str): The close character.

        Returns:
            bool: True if the characters form a valid pair, False otherwise.
        """
        if open == '(' and close == ')':
            return True
        if open == '[' and close == ']':
            return True
        if open == '{' and close == '}':
            return True
        

    def valid_parentheses(self, expression):
        """
        Check the validity of a parentheses expression.

        Args:
            expression (str): The input expression to be validated.

        Returns:
            bool: True if the expression is valid, False otherwise.
        """
        stack =[]
        for exp in expression: 
            if exp == '(' or exp =='{' or exp == '[':
                stack.append(exp)

            elif exp == ')' or exp == '}' or exp == ']':
                if len(stack) == 0 or not self.are_pair(stack[-1], exp): 
                    return False 

                else : 
                    stack.pop()

        return len(stack) == 0

expression = input('Expression: ')
s = Solution()
print(s.valid_parentheses(expression))     