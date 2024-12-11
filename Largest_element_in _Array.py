from typing import List
class Solution:
    def largest(self, arr : List[int]) -> int:
            max_element = arr[0]
            for num in arr[1:]:
                if num > max_element:
                    max_element = num
            return max_element
