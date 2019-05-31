class Solution:
    """
    给定两个字符串 s 和 t，判断它们是否是同构的。
    如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
    所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

    示例 1:

        输入: s = "egg", t = "add"
        输出: true

    示例 2:

        输入: s = "foo", t = "bar"
        输出: false

    示例 3:

        输入: s = "paper", t = "title"
        输出: true
        说明:
        你可以假设 s 和 t 具有相同的长度。
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        for idx, ch in enumerate(s):
            d1[ch] = t[idx]
        d2 = {}
        for idx, ch in enumerate(t):
            d2[ch] = s[idx]
        return ''.join(map(lambda x: d1[x], s)) == t and ''.join(map(lambda x: d2[x], t)) == s


if __name__ == '__main__':
    tests = [
        ('egg', 'add', True),
        ('foo', 'bar', False),
        ('paper', 'title', True),
        ('ab', 'aa', False),
    ]
    # TODO 这种方式性能很差
    for s, t, r in tests:
        assert Solution().isIsomorphic(s, t) == r