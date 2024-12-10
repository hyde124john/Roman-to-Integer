class Solution:
    def printFibb(self,n):
         if n <= 0:
             return []
         elif n == 1:
             return [1]
         fib_sequence = [1, 1]
         for i in range(2, n):
             next_fib = fib_sequence[-1] + fib_sequence[-2]
             fib_sequence.append(next_fib)
         return fib_sequence
