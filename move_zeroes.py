class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroIndex = 0  
        for i in range(len(nums)):
            if nums[i] != 0: 
                nums[lastNonZeroIndex], nums[i] = nums[i], nums[lastNonZeroIndex]
                lastNonZeroIndex += 1  
