from typing import List


class Solution:
    """
    我们把符合下列属性的数组 A 称作山脉：

    A.length >= 3
    存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

    示例 1：

        输入：[0,1,0]
        输出：1

    示例 2：

        输入：[0,2,1,0]
        输出：1

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/peak-index-in-a-mountain-array
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        """
        遍历实现
        :param nums:
        :return:
        """
        for idx, n in enumerate(nums):
            if nums[idx - 1] < n and nums[idx + 1] < n:
                return idx


if __name__ == '__main__':
    tests = [
        ([0, 1, 0], 1),
        ([0, 2, 1, 0], 1),
    ]
    for nums, idx in tests:
        assert Solution().peakIndexInMountainArray(nums) == idx
