# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # 防止溢出
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # 如果没有找到目标值

# 例子
# 创建一个 Solution 类的实例
sol = Solution()
# 定义一个有序数组
nums = [-1, 0, 3, 5, 9, 12]
# 定义一个目标值
target = 9
# 调用 search 方法并打印结果
print(sol.search(nums, target))  # 应该输出 4，因为 9 在数组中的下标为 4
