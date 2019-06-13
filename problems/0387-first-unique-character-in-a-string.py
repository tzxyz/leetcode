class Solution:
    """
    给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

    案例:

        s = "leetcode"
        返回 0.

        s = "loveleetcode",
        返回 2.
 
    注意事项：您可以假定该字符串只包含小写字母。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def firstUniqChar(self, s: str) -> int:
        """
        遍历字符串中的字符，如果满足以下两个条件，则返回idx
        1. 该字符不存在于 s[:idx]
        2. 该字符不存在于 s[idx + 1:]
        :param s:
        :return:
        """
        for idx, c in enumerate(s):
            if c not in s[idx + 1:] and c not in s[:idx]:
                return idx
        return -1

    def firstUniqChar2(self, s: str) -> int:
        """
        1. 将所有字符存入dict，value表示出现的次数
        2. 从头遍历一次字符串，第一次出现 value = 1 的字符就是要找字符
        :param s:
        :return:
        """
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1
        for c in s:
            if m[c] == 1:
                return s.index(c)
        return -1


if __name__ == '__main__':
    tests = [
        ('leetcode', 0),
        ('loveleetcode', 2),
        ('cc', -1),
        ('z', 0),
        ('aadadaad', -1)
    ]
    for i, o in tests:
        assert Solution().firstUniqChar(i) == o
        assert Solution().firstUniqChar2(i) == o
