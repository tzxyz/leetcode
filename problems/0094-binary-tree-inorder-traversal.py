from typing import List
from problems.bst import TreeNode
from problems.bst import list2bst


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
        递归解法，先访问左子树，再打印节点，再访问右子树
        :param root:
        :return:
        """
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        使用栈的方式
        1. 申请一个栈 stack，将 root 压栈
        2. 将左子树压栈，直到左子树为空
        3.
        :param root:
        :return:
        """
        cursor, stack, result = root, [], []
        while stack or cursor is not None:
            # 将root以及左子树压栈
            while cursor is not None:
                stack.append(cursor)
                cursor = cursor.left
            # 弹栈打印节点
            cursor = stack.pop(-1)
            result.append(cursor.val)
            # 赋值cursor
            cursor = cursor.right
        return result


if __name__ == '__main__':
    tests = [
        ([1, 2, 3], [2, 1, 3])
    ]
    for i, o in tests:
        print(Solution().inorderTraversal(list2bst(i)))
        print(Solution().inorderTraversal2(list2bst(i)))
