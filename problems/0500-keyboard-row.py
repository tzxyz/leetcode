from typing import List


class Solution:
    """
    给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。

    示例：

        输入: ["Hello", "Alaska", "Dad", "Peace"]
        输出: ["Alaska", "Dad"]

    注意：

        你可以重复使用键盘上同一字符。
        你可以假设输入的字符串将只包含字母。
    """

    def __init__(self):
        self._words = {
            'q': 1,
            'w': 1,
            'e': 1,
            'r': 1,
            't': 1,
            'y': 1,
            'u': 1,
            'i': 1,
            'o': 1,
            'p': 1,
            'a': 2,
            's': 2,
            'd': 2,
            'f': 2,
            'g': 2,
            'h': 2,
            'j': 2,
            'k': 2,
            'l': 2,
            'z': 3,
            'x': 3,
            'c': 3,
            'v': 3,
            'b': 3,
            'n': 3,
            'm': 3,
        }

    def findWords(self, words: List[str]) -> List[str]:
        r = []
        for word in words:
            x = self._words[word[0].lower()] * len(word)
            y = sum(self._words[c.lower()] for c in word)
            if x == y:
                r.append(word)
        return r


if __name__ == '__main__':
    tests = [
        (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"])
    ]
    for i, o in tests:
        assert Solution().findWords(i) == o
