
class Solution:
    def removeElement(self, nums, val):
        val_count = 0
        stack = []
        
        for num in nums:
            if num == val:
                val_count += 1
            else:
                stack.append(num)
        
        stack.append(len(stack))
        length = len(stack)
        for _ in range(val_count):
            stack.append('_')

        return length , stack

s = Solution()
result = s.removeElement([0,1,2,2,3,0,4,2], 2)
print(result)
