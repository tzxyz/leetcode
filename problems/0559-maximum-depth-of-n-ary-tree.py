class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    """
    给定一个 N 叉树，找到其最大深度。

    最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

    例如，给定一个 3叉树 :

    {"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}

    我们应返回其最大深度，3。

    说明:

    树的深度不会超过 1000。
    树的节点总不会超过 5000。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def maxDepth(self, root: 'Node') -> int:
        """
        递归，思路与求二叉树最大深度一致
        """
        if root:
            return 1 + max([self.maxDepth(c) for c in root.children] + [0])
        else:
            return 0
