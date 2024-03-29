from typing import List
from math import (log, ceil)


class Solution:
    """
    给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
    返回值小于或等于 bound 的所有强整数组成的列表。
    你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

    示例 1：

        输入：x = 2, y = 3, bound = 10
        输出：[2,3,4,5,7,9,10]

    解释：
        2 = 2^0 + 3^0
        3 = 2^1 + 3^0
        4 = 2^0 + 3^1
        5 = 2^1 + 3^1
        7 = 2^2 + 3^1
        9 = 2^3 + 3^0
        10 = 2^0 + 3^2

    示例 2：

        输入：x = 3, y = 5, bound = 15
        输出：[2,4,6,8,10,14]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/powerful-integers
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        """
        1. 使用math.log 计算出 i 的上界限 a , x ** i <= bound
        2. 使用math.log 计算出 j 的上界限 b , y ** j <= bound
        3. 列表推导所有符合条件的 (i, j) 组合
        4. 计算出强整数
        :param x:
        :param y:
        :param bound:
        :return:
        """
        a = ceil(log(bound, x)) if x != 1 else 1
        b = ceil(log(bound, y)) if y != 1 else 1
        args = ((i, j) for i in range(a) for j in range(b) if x ** i + y ** j <= bound)
        s = set()
        for i, j in args:
            s.add(x ** i + y ** j)
        return list(s)


if __name__ == '__main__':
    tests = [
        (2, 3, 10, [2, 3, 4, 5, 7, 9, 10]),
        (3, 5, 15, [2, 4, 6, 8, 10, 14]),
        (1, 2, 1000000,
         [2, 3, 5, 9, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097, 8193, 16385, 32769, 65537, 131073, 262145, 524289])
    ]
    for x, y, bound, res in tests:
        assert sorted(Solution().powerfulIntegers(x, y, bound)) == res
