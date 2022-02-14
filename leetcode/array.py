# 1. Container with most water

from typing import Dict, List, Tuple

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        
        for index_o, h_out in enumerate(height):
            index_l = [i - index_o for i in range(index_o + 1, len(height))]
            height_l = height[index_o + 1:]
            area = max([a*b for a, b in zip(index_l, height_l)])
            if area > max_area:
                max_area = area


# 17. Letter Combinations of a Phone Number

from string import ascii_lowercase

class Solution:
    phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqr',
        '8': 'stu',
        '9': 'vwxy'
    }

    def _dfs(self, digits, start, res, cur):
        if start == len(digits):
            res.append(''.join(cur))
            return
        for ch in Solution.phone[digits[start]]:
            cur.append(ch)
            print('cur is =>', cur)
            self._dfs(digits, start + 1, res, cur)
            cur.pop()


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        self._dfs(digits, 0, res, [])
        return res


### Validate Binary Search Tree
# 26. Remove Duplicates from Sorted Array

class Solution:
    def rmv(self, nums, index):
        cur = nums[index]
        if index + 1 <= len(nums) - 1 and cur <= nums[index + 1]:
            if nums[index + 1] == cur:
                nums.append(nums.pop(index + 1))
            else:
                index += 1
            self.rmv(nums, index)
        return nums

    def removeDuplicates(self, nums: List) -> int:
        if len(nums) > 1:
            return self.rmv(nums, 0)
        else:
            return nums
        
