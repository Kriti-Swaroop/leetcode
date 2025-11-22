#THIS CODE IS RELATED TO PROBLEM 3190. Find Minimum Operations to Make All Elements Divisible by Three IN LEETCODE
#BELOW IS THE PROBLEM STATEMENT FOR REFERENCE
#TOPIC: MATH
'''You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
Return the minimum number of operations to make all elements of nums divisible by 3.'''

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(num%3 !=0 for num in nums)
    ''' count=0
        for i in nums:
            if i%3==0:
                continue
            elif (i+1)%3==0 or (i-1)%3==0:
                count = count+1
        return count'''
        
