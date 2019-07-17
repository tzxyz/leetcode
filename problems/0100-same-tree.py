from problems.bst import TreeNode
from problems.bst import list2bst


class Solution:
    """
    给定两个二叉树，编写一个函数来检验它们是否相同。
    如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

    示例 1:

        输入:       1         1
                  / \       / \
                 2   3     2   3

                [1,2,3],   [1,2,3]

    输出: true

    示例 2:

        输入:      1          1
                  /           \
                 2             2

                [1,2],     [1,null,2]

    输出: false

    示例 3:

        输入:       1         1
                  / \       / \
                 2   1     1   2

                [1,2,1],   [1,1,2]

    输出: false

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/same-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        递归：节点值是否相等 && 左子节点是否相等 && 右子节点是否相等
        """
        if p is None or q is None:
            return p == q
        else:
            return p.val == q.val and \
                   self.isSameTree(p.left, q.left) and \
                   self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    tests = [
        ([1, 2], [1, None, 2], False),
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2, 1], [1, 1, 2], False),
    ]
    for p, q, result in tests:
        assert Solution().isSameTree(list2bst(p), list2bst(q)) == result
