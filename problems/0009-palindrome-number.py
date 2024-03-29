class Solution:
    """
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:

        输入: 121
        输出: true

    示例 2:

        输入: -121
        输出: false
        解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

    示例 3:

        输入: 10
        输出: false
        解释: 从右向左读, 为 01 。因此它不是一个回文数。

    进阶:
        你能不将整数转为字符串来解决这个问题吗？
    """
    def isPalindrome(self, x: int) -> bool:
        """
        转换成字符串后对比 s[idx], s[len(s) - idx - 1] 是否相等，如果不等就不是回文数
        更简洁的方法 ===> return str(x) == str(x)[::-1]
        :param x:
        :return:
        """
        s = str(x)
        for idx, n in enumerate(s):
            if s[idx] != s[len(s) - idx - 1]:
                return False
        return True


if __name__ == '__main__':
    tests = [
        (121, True),
        (-121, False),
        (10, False),
    ]
    for i, o in tests:
        assert Solution().isPalindrome(i) == o