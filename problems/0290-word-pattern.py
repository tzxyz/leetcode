class Solution:
    """
    给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
    这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

    示例1:

        输入: pattern = "abba", str = "dog cat cat dog"
        输出: true

    示例 2:

        输入:pattern = "abba", str = "dog cat cat fish"
        输出: false
    示例 3:

        输入: pattern = "aaaa", str = "dog cat cat dog"
        输出: false
    示例 4:

        输入: pattern = "abba", str = "dog dog dog dog"
        输出: false

    说明:
    你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/word-pattern
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        1. pattern 的长度和 str.split(' ') 一定是一致的
        2. 按照 idx 建立 pattern 中字符到 words 中的映射
        3. 保证映射的 k, v 都不能重复（ 有相同 key 或 value 即不符合条件）
        :param pattern:
        :param str:
        :return:
        """
        d, words = {}, str.split(' ')
        if len(pattern) != len(words):
            return False
        for idx in range(len(pattern)):
            key = pattern[idx]
            value = words[idx]
            print(d)
            if key not in d.keys():
                if value not in d.values():
                    d[key] = value
                else:
                    return False
            else:
                if value != d[key]:
                    return False
        return True


if __name__ == '__main__':
    tests = [
        ('abba', 'dog cat cat dog', True),
        ('abba', 'dog cat cat fish', False),
        ('aaaa', 'dog cat cat dog', False),
        ('abba', 'dog dog dog dog', False),
    ]
    for p, s, result in tests:
        assert Solution().wordPattern(p, s) == result