from typing import List


class Solution:
    """
    给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

    示例 1:

        给定 nums = [3, 2, 2, 3], val = 3,
        函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
        你不需要考虑数组中超出新长度后面的元素。

    示例 2:

        给定 nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2,
        函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
        注意这五个元素可为任意顺序。
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        重数组头部开始遍历，如果值等于val则删除
        :param nums:
        :param val:
        :return:
        """
        idx, l = 0, len(nums)
        while idx < l:
            if nums[idx] == val:
                nums.remove(val)
                l -= 1
            else:
                idx += 1

        return len(nums)

    def removeElement2(self, nums: List[int], val: int) -> int:
        """
        就结果而言这种写法也是对对，leetcode判错
        :param nums:
        :param val:
        :return:
        """
        return len(list(filter(lambda x: x != val, nums)))


if __name__ == '__main__':
    tests = [
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
    ]
    for ns, v, r in tests:
        assert Solution().removeElement(nums=ns, val=v) == r
