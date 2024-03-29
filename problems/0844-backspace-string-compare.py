class Solution:
    """
    给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

    示例 1：

        输入：S = "ab#c", T = "ad#c"
        输出：true
        解释：S 和 T 都会变成 “ac”。

    示例 2：

        输入：S = "ab##", T = "c#d#"
        输出：true
        解释：S 和 T 都会变成 “”。

    示例 3：

        输入：S = "a##c", T = "#a#c"
        输出：true
        解释：S 和 T 都会变成 “c”。

    示例 4：

        输入：S = "a#c", T = "b"
        输出：false
        解释：S 会变成 “c”，但 T 仍然是 “b”。

    提示：

        1 <= S.length <= 200
        1 <= T.length <= 200
        S 和 T 只含有小写字母以及字符 '#'。
    """

    def backspaceCompare(self, S: str, T: str) -> bool:
        s1 = []
        s2 = []
        for c in S:
            if c is '#':
                if s1:
                    s1.pop(-1)
            else:
                s1.append(c)
        for c in T:
            if c is '#':
                if s2:
                    s2.pop(-1)
            else:
                s2.append(c)
        return s1 == s2


if __name__ == '__main__':
    tests = {
        ('ab#c', 'ad#c'),
        ('ab##', 'c#d#'),
        ('a##c', '#a#c'),
        ('a#c', 'b'),
    }
    for (s, t) in tests:
        print(Solution().backspaceCompare(s, t))
