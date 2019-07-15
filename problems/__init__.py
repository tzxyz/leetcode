import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list2bst(values):
    """
    数组 转 二叉树，方便调试
    :param values:
    :return:
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = collections.deque([root])
    size = len(values)
    nums = 1
    while nums < size:
        node = queue.popleft()
        if node:
            node.left = TreeNode(values[nums]) if values[nums] else None
            queue.append(node.left)
            if nums + 1 < size:
                node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                queue.append(node.right)
                nums += 1
            nums += 1
    return root
