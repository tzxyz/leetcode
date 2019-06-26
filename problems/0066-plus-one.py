from typing import List


class Solution:
    """
    给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
    最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
    你可以假设除了整数 0 之外，这个整数不会以零开头。

    示例 1:

        输入: [1,2,3]
        输出: [1,2,4]
        解释: 输入数组表示数字 123。

    示例 2:

        输入: [4,3,2,1]
        输出: [4,3,2,2]
        解释: 输入数组表示数字 4321。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/plus-one
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        将digits转换成数字 +1 后转回数组
        :param digits:
        :return:
        """
        n = int(''.join(map(str, digits))) + 1
        result = []
        while n > 0:
            d = n % 10
            n = n // 10
            result.insert(0, d)
        return result


if __name__ == '__main__':
    tests = [
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
        ([1, 9], [2, 0]),
    ]
    for before, after in tests:
        print(Solution().plusOne(before))