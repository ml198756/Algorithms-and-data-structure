## 数组中没有重复的数字
class Solution:
    def Twosums(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    result.append([i, j])
        return result

solution = Solution()
nums = [2, 3, 5, 4, 5, 3]
target = 7
result = solution.Twosums(nums, target)
print(solution.Twosums(nums, target))
                


