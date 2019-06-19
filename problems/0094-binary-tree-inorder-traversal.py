from typing import List


class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个二叉树，返回它的中序 遍历。

    示例:

        输入: [1,null,2,3]
           1
            \
             2
            /
           3

    输出: [1,3,2]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归解法
        :param root:
        :return:
        """
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node1.left = node2
    root.right = node1
    print(Solution().inorderTraversal(root))
