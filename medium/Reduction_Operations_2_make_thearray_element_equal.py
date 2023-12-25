class Solution:
    def reductionOperations(self):
        nums = [5,1,3]


        nums_with_indices = list(enumerate(nums))

        for i in range(len(nums_with_indices)):
            for j in range(len(nums_with_indices) - i - 1):
                if nums_with_indices[j][1] > nums_with_indices[j+1][1]:
                    nums_with_indices[j], nums_with_indices[j+1] = nums_with_indices[j+1], nums_with_indices[j]

        largest = nums_with_indices[-1]
        next_largest = nums_with_indices[-2]

        

        largest = next_largest
        nums_with_indices[-1] = largest

        var = self.index_next_largest(nums_with_indices, next_largest)


        return var

    def index_next_largest(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return nums[i][0]  

s = Solution()
print(s.reductionOperations())
