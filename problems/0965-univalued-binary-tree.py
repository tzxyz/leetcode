from problems.bst import TreeNode
from problems.bst import list2bst


class Solution:
    """
    如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
    只有给定的树是单值二叉树时，才返回 true；否则返回 false。

    示例 1：

        输入：[1,1,1,1,1,null,1]
        输出：true

    示例 2：

        输入：[2,2,2,5,2]
        输出：false
 
    提示：

        给定树的节点数范围是 [1, 100]。
        每个节点的值都是整数，范围为 [0, 99] 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/univalued-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def isUnivalTree(self, root: TreeNode) -> bool:
        """
        遍历二叉树，如果节点值不等于 root 的节点值，返回false
        :param root:
        :return:
        """
        value, stack = root.val, []
        stack.append(root)
        while stack:
            cursor = stack.pop(-1)
            if cursor is None:
                continue
            else:
                if cursor.val != value:
                    return False
                if cursor.left is not None:
                    stack.append(cursor.left)
                if cursor.right is not None:
                    stack.append(cursor.right)
        return True


if __name__ == '__main__':
    tests = [
        ([1, 1, 1, 1, 1, None, 1], True),
        ([1, 1, 1, 1, 3, None, 1], False),
    ]
    for i, o in tests:
        assert Solution().isUnivalTree(list2bst(i)) == o
