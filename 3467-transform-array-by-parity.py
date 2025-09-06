# https://leetcode.com/problems/transform-array-by-parity

from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd = 0
        even = 0
        
        for num in nums:
            if num % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
        
        return [0] * even + [1] * odd