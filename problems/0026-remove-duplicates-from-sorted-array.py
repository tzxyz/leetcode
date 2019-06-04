from typing import List


class Solution:
    """
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

    示例 1:

        给定数组 nums = [1,1,2],
        函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
        你不需要考虑数组中超出新长度后面的元素。

    示例 2:
        给定 nums = [0,0,1,1,1,2,2,3,3,4],
        函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
        你不需要考虑数组中超出新长度后面的元素。
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        这是一个排好序的数组，当大于2个元素时，对比头两个元素，相同则删除，不同下标后移动一位对比
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return 1
        else:
            idx, size = 0, len(nums)
            while idx < size - 1:
                if nums[idx] == nums[idx + 1]:
                    nums.pop(idx)
                    size -= 1
                else:
                    idx += 1
        return len(nums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        """
        从第一个元素开始遍历，如果index返回的索引值和rindex相加等于len-1，说明没有重复元素，否则把重复删除
        超时（160／161）
        :param nums:
        :return:
        """
        idx = 0
        l = len(nums)
        while idx < l:
            n = nums[idx]
            while nums.index(n) + nums[::-1].index(n) != l - 1:
                nums.remove(n)
                l = len(nums)
            idx += 1
        return len(nums)


    def removeDuplicates3(self, nums: List[int]) -> int:
        """
        从第一个元素开始遍历，如果它存在在数组之后的部分，那么就删除它（超时 160／161）
        :param nums:
        :return:
        """
        idx = 0
        size = len(nums)
        while idx < size:
            head = nums[idx]
            if head in nums[idx + 1:]:
                nums.pop(idx)
                idx = 0
                size = len(nums)
            else:
                idx += 1
        return len(nums)


if __name__ == '__main__':
    tests = [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)
    ]
    for ns, l in tests:
        assert Solution().removeDuplicates(ns) == l
