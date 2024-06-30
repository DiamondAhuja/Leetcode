# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def revInorder(root):
            nonlocal x
            if root:
                revInorder(root.right)
                x += root.val
                root.val = x
                revInorder(root.left)

        x = 0
        revInorder(root)

        return root
