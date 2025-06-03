class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        if len(s) == 0 or not s or s.strip() == "": return True
        if len(s) % 2: return False
        st = ""
        for c in s:
            if c.isalnum():
                st += c
        st = st.lower()
        left, right = 0, len(st) - 1
        while left < right:
            if st[left] != st[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    # print(isPalindrome("A man, a plan, a canal: Panama"))
    # print(isPalindrome("0P"))

    @staticmethod
    def twoSum(numbers: list[int], target: int) -> list[int]:
        if len(numbers) == 2 and numbers[0] + numbers[1] == target: return [1, 2]
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

    @staticmethod
    def threeSum(nums: list[int]) -> list[list[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            target = 0 - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        result = [list(t) for t in {tuple(sorted(lst)) for lst in res}]
        return result

    print(threeSum([-1, 0, 1, 2, -1, -4]))
