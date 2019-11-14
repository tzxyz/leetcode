from typing import List


class Solution:
    """
    给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

    函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

    说明:

        返回的下标值（index1 和 index2）不是从零开始的。
        你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

    示例:

        输入: numbers = [2, 7, 11, 15], target = 9
        输出: [1,2]

    解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        1. 数组有序
        2. 使用双指针 start, end 分别表示数组的第一个元素(最小)和最后一个元素(最大)
        3. 如果 numbers[start] + numbers[end] = target 表示找到了这两个数
        4. 如果 numbers[start] + numbers[end] < target，说明数小了，尝试放大最小的数，start += 1
        5. 如果 numbers[start] + numbers[end] > target，说明数大了，尝试缩小最大的数，end   -= 1
        6. 直到 numbers[start] + numbers[end] = target 为止
        """
        start, end = 0, len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
