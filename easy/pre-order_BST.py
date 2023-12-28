from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorderTraversalRecursive(root, result)
        return result
    
    def preorderTraversalRecursive(self, root: Optional[TreeNode], result: List[int]) -> None:
        if root:
            result.append(root.val)
            self.preorderTraversalRecursive(root.left, result)
            self.preorderTraversalRecursive(root.right, result)

if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)


    solution_instance = Solution()


    result = solution_instance.preorderTraversal(root)


    print(result)
