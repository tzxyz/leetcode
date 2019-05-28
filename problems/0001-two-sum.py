from typing import List


class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    示例:

        给定 nums = [2, 7, 11, 15], target = 9
        因为 nums[0] + nums[1] = 2 + 7 = 9
        所以返回 [0, 1]
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in d.keys():
                return [d[diff], i]
            d[x] = i

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i + 1:]):
                if x + y == target:
                    print(x, y)
                    return [i, j + i + 1]


if __name__ == '__main__':
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 3], 6, [0, 1]),
        ([3, 2, 4], 6, [1, 2])
    ]
    for n, t, r in tests:
        assert Solution().twoSum(n, t) == r
