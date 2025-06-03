import heapq
from collections import defaultdict, OrderedDict

from fontTools.qu2cu.qu2cu import Solution


class Solution:

    @staticmethod
    def containsDuplicate(nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)

    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if not s and not t: return True
        if len(s) != len(t):
            return False
        else:
            return sorted(s) == sorted(t)

    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums:
                j = nums.index(complement)
                if i != j:
                    return [i, j]

    @staticmethod
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        if not strs: return [[""]]
        if len(strs) == 1: return [strs]
        res = defaultdict(set)
        for st in strs:
            tmp = sorted(st)
            if st not in res: res[tmp].add(st)
        return [list(s) for s in res.values()]

    @staticmethod
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        if not nums or k > len(nums): return []
        d = OrderedDict()
        apperances = OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        res = []
        for num in nums:
            if num not in apperances.keys():
                apperances[num] = 1
            else:
                apperances[num] += 1
        print(apperances)
        res = [key for key, _ in heapq.nlargest(k, apperances.items(), key=lambda x: x[1])]
        return res

    # print(topKFrequent([3,0,1,0],1))

    @staticmethod
    def productExceptSelf(nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        if not nums: return res
        for i in range(n):
            res[i] = nums[(i + 1) % n] * nums[(i + 2) % n]
        # res[-1]=nums[0]*nums[1]
        print("res is: ", res)
        for i in range(n - 1, -1, -1):
            res[i] *= nums[(i - 1) % n]
        return res

    # print(productExceptSelf([1,2,3,4])) #should be [24,12,8,6]
    # print(productExceptSelf([-1,-1,0,-3,3])) #should be [0,0,9,0,0]

    # @staticmethod
    # def isValidSudoku( board: list[list[str]]) -> bool:
    #     d = {i: False for i in range(1, 10)}
    #     for j in range(9):
    #         for i in range(9):
    #             if not d[int(board[i][j])]:
    #                 d[i]=True
    #             else:
    #                 return False
    #         d = {k: False for k in d}
    #

    @staticmethod
    def longestConsecutive(nums: list[int]) -> int:
        if not nums: return 0
        heapq.heapify(nums)
        # print(nums)
        n = len(nums)
        max_len = 1
        curr_max = max_len
        prev = heapq.heappop(nums)
        while nums:
            if prev == nums[0] - 1:
                curr_max += 1
            elif prev == nums[0]:
                heapq.heappop(nums)
                continue
            else:
                max_len = max(max_len, curr_max)
                curr_max = 1
            prev = heapq.heappop(nums)
        return max(max_len, curr_max)

    print(longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
