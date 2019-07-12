from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个二叉树，返回它的 前序 遍历。

    示例:

        输入: [1,null,2,3]
           1
            \
             2
            /
           3

    输出: [1,2,3]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        else:
            return []

