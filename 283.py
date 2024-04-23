def moveZeroes(nums):
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums

# 测试
nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))  # Output: [1, 3, 12, 0, 0]

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        left = 0
        
        for right in range(n):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        return nums

#测试
nums = [1, 3, 0, 0, 12, 0, 18]
print(moveZeroes(nums))