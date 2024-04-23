# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1  # 结果数组从后向前填充

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1
            pos -= 1
        
        return result

# 示例使用
sol = Solution()
nums = [-4, -1, 0, 3, 10]
print(sol.sortedSquares(nums))  # 输出应为 [0, 1, 9, 16, 100]
