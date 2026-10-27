# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def depth(self, root):

        if root is None:
            return 0


        left_child = self.depth(root.left) + 1
        right_child = self.depth(root.right) + 1

        if left_child > right_child:
            return left_child
        return right_child


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)