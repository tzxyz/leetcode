from typing import List


class Solution:
    """
    给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

    示例 1:

        输入: nums = [1,2,3,1], k = 3
        输出: true

    示例 2:

        输入: nums = [1,0,1,1], k = 1
        输出: true

    示例 3:

        输入: nums = [1,2,3,1,2,3], k = 2
        输出: false
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for idx, n in enumerate(nums):
            # d.get(n)不为空时，idx一定大于n
            if d.get(n) is not None:
                x = abs(idx - d[n])
                if x <= k:
                    return True
                else:
                    d[n] = idx
            else:
                d[n] = idx
        return False


if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
        ([99, 99], 2, True),
    ]
    for nums, k, r in tests:
        assert Solution().containsNearbyDuplicate(nums, k) == r
