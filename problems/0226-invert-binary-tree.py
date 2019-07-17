from problems.bst import TreeNode
from problems.bst import list2bst


class Solution:
    """
    翻转一棵二叉树。

    示例：

        输入：

             4
           /   \
          2     7
         / \   / \
        1   3 6   9

    输出：

             4
           /   \
          7     2
         / \   / \
        9   6 3   1

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/invert-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        递归思路：
        1. 翻转节点的左子树，右子树
        2. 将节点的 left，right 互换
        3. 直到翻转到叶子节点
        """
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root


if __name__ == '__main__':
    tests = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1])
    ]
    for i, o in tests:
        print(Solution().invertTree(list2bst(i)))
