from problems.bst import TreeNode
from problems.bst import list2bst


class Solution:
    """
    给定二叉搜索树（BST）的根节点和一个值。
    你需要在BST中找到节点值等于给定值的节点。
    返回以该节点为根的子树。
    如果节点不存在，则返回 NULL。

    例如，

        给定二叉搜索树:

                4
               / \
              2   7
             / \
            1   3

    和值: 2

    你应该返回如下子树:

              2
             / \
            1   3

    在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/search-in-a-binary-search-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cursor = root
        while cursor:
            if cursor.val == val:
                return cursor
            elif cursor.val < val:
                cursor = cursor.right
            else:
                cursor = cursor.left


if __name__ == '__main__':
    tests = [
        ([4, 2, 7, 1, 3, None, None], 2, list2bst([2, 1, 3])),
        ([2, 1, 3], 5, list2bst([]))
    ]
    for i, v, o in tests:
        print(Solution().searchBST(list2bst(i), v))
