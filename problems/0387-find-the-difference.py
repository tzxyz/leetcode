class Solution:
    """
    给定两个字符串 s 和 t，它们只包含小写字母。
    字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
    请找出在 t 中被添加的字母。

    示例:

    输入：
        s = "abcd"
        t = "abcde"

    输出：
        e

    解释：
        'e' 是那个被添加的字母。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/find-the-difference
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def findTheDifference(self, s: str, t: str) -> str:
        """
        将 t 转换成字符数组，把存在 s 中的字符删除
        :param s:
        :param t:
        :return:
        """
        tc = list(t)
        for c in s:
            tc.remove(c)
        return ''.join(tc)


if __name__ == '__main__':
    tests = [
        ('abcd', 'abcde', 'e'),
        ('a', 'aa', 'a')
    ]
    for s, t, c in tests:
        assert Solution().findTheDifference(s, t) == c
