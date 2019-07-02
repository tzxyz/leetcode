# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
    二叉搜索树保证具有唯一的值。

    示例 1：

        输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
        输出：32

    示例 2：

        输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
        输出：23
 
    提示：

        树中的结点数量最多为 10000 个。
        最终的答案保证小于 2^31。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/range-sum-of-bst
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """
        递归，如果当前节点的值在 L <= root.val <= R 之间，取root.val，否则取0
        :param root:
        :param L:
        :param R:
        :return:
        """
        if root is None:
            return 0
        else:
            ls = self.rangeSumBST(root.left, L, R)
            rs = self.rangeSumBST(root.right, L, R)
            ms = root.val if root.val is not None and L <= root.val <= R else 0
            return ms + ls + rs


if __name__ == '__main__':
    a = [10, 5, 15, 3, 7, None, 18]
    root = TreeNode(10)
    l1 = TreeNode(5)
    r1 = TreeNode(15)
    l2 = TreeNode(3)
    r2 = TreeNode(7)
    l3 = TreeNode(None)
    r3 = TreeNode(18)

    r1.left = l3
    r1.right = r3

    l1.left = l2
    l1.right = r2

    root.left = l1
    root.right = r1

    total = Solution().rangeSumBST(root, 7, 15)
    print(total)
