from typing import List


class Solution:
    """
    给定一个整数数组，判断是否存在重复元素。
    如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

    示例 1:

        输入: [1,2,3,1]
        输出: true

    示例 2:

        输入: [1,2,3,4]
        输出: false

    示例 3:

        输入: [1,1,1,3,3,4,3,2,4,2]
        输出: true
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate2(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d.keys():
                return True
            else:
                d[n] = True
        return False


if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
    ]
    for nums, r in tests:
        assert Solution().containsDuplicate(nums) == r
        assert Solution().containsDuplicate2(nums) == r
