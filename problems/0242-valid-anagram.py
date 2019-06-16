class Solution:
    """
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

    示例 1:

        输入: s = "anagram", t = "nagaram"
        输出: true

    示例 2:

        输入: s = "rat", t = "car"
        输出: false

    说明:
        你可以假设字符串只包含小写字母。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/valid-anagram
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """
        将 s 中的字符存入一个字典 d , key 为字符, value 为该字符出现的次数
        将 t 中的字符出现的次数递减
        如果是异位字符串，那么 d 中最后每个字符出现的次数为0
        :param s:
        :param t:
        :return:
        """
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            d[c] = d.get(c, 0) - 1
        for v in d.values():
            if v != 0:
                return False
        return True


if __name__ == '__main__':
    tests = [
        ('anagram', 'nagaram', True),
        ('rat', 'car', False),
    ]
    for s, t, result in tests:
        assert Solution().isAnagram(s, t) == result