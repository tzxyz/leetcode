# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个二叉树，找出其最小深度。
    最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

    说明: 
        叶子节点是指没有子节点的节点。

    示例:

        给定二叉树 [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回它的最小深度  2.

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def minDepth(self, root: TreeNode) -> int:
        """
        递归，返回 1 + min(左子树深度， 右子树深度)，需要判断如果左或右子树为空， 取不为空的作为最小值
        :param root:
        :return:
        """
        if root is not None:
            ld = self.minDepth(root.left)
            rd = self.minDepth(root.right)
            if ld == rd == 0:
                md = 0
            elif ld == 0 and rd != 0:
                md = rd
            elif rd == 0 and ld != 0:
                md = ld
            else:
                md = min(ld, rd)
            return 1 + md
        else:
            return 0


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    root.left = left
    print(Solution().minDepth(root))
