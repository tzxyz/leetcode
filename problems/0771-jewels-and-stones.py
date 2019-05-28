class Solution:
    """
    给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
    J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

    示例 1:

        输入: J = "aA", S = "aAAbbbb"
        输出: 3

    示例 2:

        输入: J = "z", S = "ZZ"
        输出: 0

    注意:

        S 和 J 最多含有50个字母。
        J 中的字符不重复。
    """

    def numJewelsInStones(self, j: str, s: str) -> int:
        d = {}
        for k in j:
            d[k] = 0
        for c in s:
            if c in d.keys():
                d[c] = d[c] + 1
        return sum(d.values())


if __name__ == '__main__':
    tests = [
        ('aA', 'aAAbbbb', 3),
        ('z', 'ZZ', 0)
    ]
    for j, s, r in tests:
        assert Solution().numJewelsInStones(j, s) is r
