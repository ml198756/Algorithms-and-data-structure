## 取反比较（运行速度快，但占用内存）
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_b = [c.lower() for c in s if c.isalnum()]
        filtered_c = ''.join(filtered_b)
        return filtered_c == filtered_c[::-1]

solution = Solution()
s = "ete, ETE"
print(solution.isPalindrome(s))

## 双指针比较(占用内存少)
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1  # 初始化左右指针

    while left < right:
        # 跳过左边的非字母数字字符
        while left < right and not s[left].isalnum():
            left += 1
        # 跳过右边的非字母数字字符
        while left < right and not s[right].isalnum():
            right -= 1

        # 比较当前的字符，如果不同，则不是回文串
        if s[left].lower() != s[right].lower():
            return False

        # 移动指针继续比较
        left += 1
        right -= 1

    return True

# 测试示例
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # 输出：True

s = "race a car"
print(isPalindrome(s))  # 输出：False

## 栈比较
def isPalindrome(s: str) -> bool:
    # 预处理字符串：转换为小写并移除非字母数字字符
    filtered_chars = [c.lower() for c in s if c.isalnum()]

    # 使用列表作为栈
    stack = []

    # 将每个字符推入栈中
    for char in filtered_chars:
        stack.append(char)

    # 从栈中弹出字符并比较
    for char in filtered_chars:
        if char != stack.pop():
            return False

    # 如果所有字符都匹配，则字符串是回文串
    return True

# 测试示例
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # 输出：True

s = "race a car"
print(isPalindrome(s))  # 输出：False

result = (for i in c if i.isalnum())
print(result)
