class Solution :
    def are_pair(self, open , close):
        if open == '(' and close == ')':
            return True
        if open == '[' and close == ']':
            return True
        if open == '{' and close == '}':
            return True
        

    def valid_parentheses(self, expression):
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