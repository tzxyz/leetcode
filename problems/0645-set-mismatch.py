from typing import List


class Solution:
    """
    集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
    给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

    示例 1:

        输入: nums = [1,2,2,4]
        输出: [2,3]

    注意:

        给定数组的长度范围是 [2, 10000]。
        给定的数组是无序的。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/set-mismatch
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        将数组转换成map，如果改数存在，则表示重复的数字。
        遍历 1-len(nums) 的数字，如果不存在map，则表示缺失的数字
        :param nums:
        :return:
        """
        d, result = {}, []
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                result.append(num)
        print(d)
        for x in range(1, len(nums) + 1):
            if x not in d:
                result.append(x)
                break
        return result

    def findErrorNums2(self, nums: List[int]) -> List[int]:
        """
        1. 先用sum(nums) - sum(set(nums))计算出重复的数字
        2. 再用range(1, len(nums) + 1) 和 nums 取差集算出丢失的数字
        :param nums:
        :return:
        """
        x = sum(nums) - sum(set(nums))
        y = (set(range(1, len(nums) + 1)) - set(nums)).pop()
        return [x, y]


if __name__ == '__main__':
    tests = [
        ([1, 2, 2, 4], [2, 3]),
        ([1, 1], [1, 2]),
        ([3, 3, 1], [3, 2]),
    ]
    for i, o in tests:
        assert Solution().findErrorNums(i) == o
        assert Solution().findErrorNums2(i) == o
