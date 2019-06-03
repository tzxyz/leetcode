# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个二叉树，找出其最大深度。

    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

    说明: 叶子节点是指没有子节点的节点。

    示例：
        给定二叉树 [3,9,20,null,null,15,7]，

        3
       / \
      9  20
        /  \
       15   7

    返回它的最大深度 3 。
    """
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
