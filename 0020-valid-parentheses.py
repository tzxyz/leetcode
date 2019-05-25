class Solution:
    """
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

    有效字符串需满足：

        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串。

    示例 1:
        输入: "()"
        输出: true

    示例 2:
        输入: "()[]{}"
        输出: true

    示例 3:
        输入: "(]"
        输出: false

    示例 4:
        输入: "([)]"
        输出: false

    示例 5:
        输入: "{[]}"
        输出: true
    """
    def isValid(self, s: str) -> bool:
        mappings = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        chars = list(s)
        stack = []
        while chars:
            c = chars.pop(0)
            if stack:
                top = stack[-1]
                if mappings.get(c) is top:
                    stack.pop(-1)
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return len(stack) == 0

    def isValid2(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        return s == ''


if __name__ == '__main__':
    tests = [
        '',
        '()',
        '()[]{}',
        '(]',
        '([)]',
        '{[]}'
    ]
    for test in tests:
        print(Solution().isValid(test))
        print(Solution().isValid2(test))
