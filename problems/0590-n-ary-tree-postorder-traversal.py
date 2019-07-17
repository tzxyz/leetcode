from typing import List


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    """
    给定一个 N 叉树，返回其节点值的后序遍历。

    例如，给定一个 3叉树 :

    返回其后序遍历: [5,6,3,2,4,1].

    说明: 递归法很简单，你可以使用迭代法完成此题吗?

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def postorder(self, root: 'Node') -> List[int]:
        if root is not None:
            if root.children is not None:
                result = []
                for child in root.children:
                    result += self.postorder(child)
                result += [root.val]
                return result
        else:
            return []

