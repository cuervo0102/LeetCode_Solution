"""
Google
In place

Given a list 'nums' and a value 'val', this method removes all occurrences of 'val' from 'nums' 
in-place and returns the length of the modified list.

:type nums: List[int]
:param nums: The input list of integers.
:type val: int
:param val: The value to be removed from the list.
:rtype: int
:return: The length of the modified list after removing 'val' in place.
"""
class Solution : 
    def remove_element(self, nums, val):
        k = 0
        for i in range(len(nums)): 
            if nums[i] != val : 
                nums[k] = nums[i]
                k += 1

        return k 
    

s = Solution()
print(s.remove_element([1,2,3,3,4,5],3))
