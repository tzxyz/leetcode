from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = {}
        for i in A:
            if i not in d.keys():
                d[i] = 1
            else:
                return i


if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 3], 3),
        ([2, 1, 2, 5, 3, 2], 2),
        ([5, 1, 5, 2, 5, 3, 5, 4], 5),
    ]
    for i, o in tests:
        assert Solution().repeatedNTimes(i) == o
