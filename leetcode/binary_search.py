from typing import List

# 1. Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def b_search(self, s, e, nums, target):
        """
            find the mid index, k, and its value nums[k]
            if nums[k] > target:
                nums[last] > nums[k], search target in index 0 ~ k
                nums[last] < nums[k], search target in index k ~ last
            elif nums[k] < target:
                nums[last] > target, search target in index k ~ last
                nums[last] < target, search target in index 0 ~ k
        """
        m = (s + e) // 2
        print('nums[m] is =>', nums[m])
        if s < e :
            if nums[m] == target:
                return m
            
            elif nums[m] > target:
                if nums[e] > nums[m]:
                    return self.b_search(s, m, nums, target)
                else:
                    if nums[s] <= target:
                        return self.b_search(s, m, nums, target)
                    else:
                        return self.b_search(m+1, e, nums, target)
                    
            elif nums[m] < target:
                if nums[e] >= target:
                    return self.b_search(m+1, e, nums, target)
                else:
                    if nums[s] <= target and nums[s] < nums[m]:
                        return self.b_search(m+1, e, nums, target)
                    elif nums[s] <= target and nums[s] > nums[m]:
                        return self.b_search(s, m, nums, target)
                    else:
                        return self.b_search(m+1, e, nums, target)
                    
        return s if target == nums[s] else -1
             
    
    
    def search(self, nums: List[int], target: int) -> int:
        
        return self.b_search(0, len(nums)-1, nums, target)
