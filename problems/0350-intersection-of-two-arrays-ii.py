from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        1. 将数组排序
        2. 判断两个指针的值是否相等
        3. 如果相等双指针+1
        4. 如果相等指针小的+1
        5. 判断条件为小数组指针到末尾，由于排序过，当小数组遍历完成，大数组一定找不到和它相等的值了
        """
        s1, s2, e1, e2 = 0, 0, len(nums1) - 1, len(nums2) - 1,
        result = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        while s1 <= e1 and s2 <= e2:
            if nums1[s1] == nums2[s2]:
                result.append(nums1[s1])
                s1 += 1
                s2 += 1
            elif nums1[s1] < nums2[s2]:
                s1 += 1
            else:
                s2 += 1
        return result


if __name__ == '__main__':
    tests = [
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([2, 2, 2, 2, 1], [2, 2, 2, 2, 2, 1], [1, 2, 2, 2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([1, 1], [], []),
        ([3, 1, 2], [1], [1]),
    ]
    s = Solution()
    for n1, n2, r in tests:
        print(s.intersect(n1, n2))
