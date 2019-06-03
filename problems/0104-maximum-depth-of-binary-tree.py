# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    n0 = TreeNode(3)
    n1 = TreeNode(9)
    n2 = TreeNode(20)
    n3 = TreeNode(15)
    n4 = TreeNode(7)
    n0.left = n1
    n0.right = n2
    n2.left = n3
    n2.right = n4
    depth = Solution().maxDepth(root=n0)
    print(depth)
