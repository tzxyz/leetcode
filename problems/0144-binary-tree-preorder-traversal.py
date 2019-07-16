from typing import List
from problems.bst import TreeNode
from problems.bst import list2bst


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
        """
        递归的方式遍历，先打印节点，再访问左子树，再访问右子树
        :param root:
        :return:
        """
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        else:
            return []

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        使用栈的方式
        1. 申请一个栈 stack，将 root 压栈
        2. 栈顶弹出一个节点，打印该节点，如果右子树不为空，将右子树压栈，如果左子树不为空，将左子树压栈。
        3. 循环，直到栈为空
        :param root:
        :return:
        """
        stack, result = [], []
        stack.append(root)
        while stack:
            top = stack.pop(-1)
            if top is not None:
                result.append(top.val)
                if top.right is not None:
                    stack.append(top.right)
                if top.left is not None:
                    stack.append(top.left)
        return result


if __name__ == '__main__':
    tests = [
        ([1, None, 2, 3], [1, 2, 3])
    ]
    for i, o in tests:
        root = list2bst(i)
        assert Solution().preorderTraversal(root) == o

