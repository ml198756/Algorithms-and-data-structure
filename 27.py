# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
# 双指针求法
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # 初始化用于跟踪非val值的位置的指针
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i  # 新数组的长度

# 例子
sol = Solution()
nums = [3, 2, 2, 3]
val = 3
new_length = sol.removeElement(nums, val)
print("New length:", new_length)
print("Modified array:", nums[:new_length])  # 输出修改后数组的有效部分


# 暴力求解
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                # 如果当前元素等于val，将后面的元素向前移动一位
                for j in range(i + 1, len(nums)):
                    nums[j - 1] = nums[j]
                # 减少数组长度
                nums.pop()
            else:
                # 只有当当前元素不等于val时，才向前移动i
                i += 1
        return len(nums)  # 返回新的数组长度

# 例子
sol = Solution()
nums = [3, 2, 2, 3]
val = 3
new_length = sol.removeElement(nums, val)
print("New length:", new_length)
print("Modified array:", nums[:new_length])  # 输出修改后数组的有效部分
