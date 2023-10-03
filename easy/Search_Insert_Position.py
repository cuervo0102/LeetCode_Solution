"""
Perform a binary search to find the index of the 'target' element in the 'nums' list or the correct insertion index if 'target' is not found.

Parameters:
    nums (list): A sorted list of integers.
    target (int): The element to search for in the 'nums' list.

Returns:
    int: If 'target' is found in 'nums', returns the index of 'target' in 'nums'.
         If 'target' is not found in 'nums', returns the index where 'target' should be inserted to maintain the sorted order.

Note:
    This function assumes that 'nums' is sorted in ascending order.
    If 'target' is not found in 'nums', the returned index represents the correct insertion point.
"""


class Solution : 
    def search_insert(self, nums, target):
        left , right =  0 , len(nums) -1 
        mid = (left + right) // 2 

        if nums[mid] == target : 
            return mid 
        
        if nums[mid] < target : 
            left = mid + 1

        if nums[mid] > target :
            right = mid - 1


        return left 
            

s = Solution()
print(s.search_insert([1,2,3,5,6],4))