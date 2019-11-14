from typing import List


class Solution:
    """
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
    如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    你可以假设数组中无重复元素。

    示例 1:

        输入: [1,3,5,6], 5
        输出: 2

    示例 2:

        输入: [1,3,5,6], 2
        输出: 1

    示例 3:

        输入: [1,3,5,6], 7
        输出: 4

    示例 4:

        输入: [1,3,5,6], 0
        输出: 0

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/search-insert-position
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        1. 如果target 大于数组最大值，返回len(nums)
        2. 否则找到数组内等于target的索引或第一个小于target的索引
        3. 数组有序且不重复，使用二分查找
        4. 注意二分法的边界线条件
        """
        start, end = 0, len(nums) - 1
        if nums[end] < target:
            return len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start


if __name__ == '__main__':
    tests = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
    ]
    s = Solution()
    for nums, target, result in tests:
        t = s.searchInsert(nums, target)
        assert t == result
