## 三数之和问题
## 用双指针求解
class ThreeSum:
    def __init__(self, nums):
        self.nums = nums

    def find_three_sum(self):
        # 对数组进行排序
        self.nums.sort()
        results = []
        n = len(self.nums)
        
        for i in range(n - 2):
            # 跳过重复的数字
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                sum = self.nums[i] + self.nums[left] + self.nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([self.nums[i], self.nums[left], self.nums[right]])
                    # 跳过重复的数字
                    while left < right and self.nums[left] == self.nums[left + 1]:
                        left += 1
                    while left < right and self.nums[right] == self.nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return results

# 使用示例
nums = [-1, 0, 1, 2, -1, -4]
three_sum_solver = ThreeSum(nums)
result = three_sum_solver.find_three_sum()
print(result)
