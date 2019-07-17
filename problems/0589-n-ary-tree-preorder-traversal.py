from typing import List


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    """
    给定一个 N 叉树，返回其节点值的前序遍历。

    例如，给定一个 3叉树 :

    {"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1} 

    返回其前序遍历: [1,3,5,6,2,4]。

    说明: 递归法很简单，你可以使用迭代法完成此题吗?

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def preorder(self, root: 'Node') -> List[int]:
        """
        前序遍历递归：
        1. print 节点
        2. 依次调用子节点
        :param root:
        :return:
        """
        if not root:
            return []
        result = [root.val]
        for child in root.children:
            result += self.preorder(child)
        return result
