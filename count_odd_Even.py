class Solution:
	def countOddEven(self, arr):
		odd_count = 0
        even_count = 0
    
        for num in arr:
            if num % 2 == 0:
                even_count += 1
            else:
                 odd_count += 1
    
        return odd_count, even_count
