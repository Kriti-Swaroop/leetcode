#THIS CODE IS RELATED TO PROBLEM 1523. Count Odd Numbers in an Interval Range IN LEETCODE
#BELOW IS THE PROBLEM STATEMENT FOR REFERENCE
#TOPIC: MATH

'''Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low) % 2 != 0:
            return ((high - low) // 2) +1
        elif low%2 == 0 and high%2 ==0:
            return (high - low) // 2
        else:
            return ((high - low) // 2) +1
           
            #3-17 e 8
            #4-18 e 7
            #3-18 o 8
            #4-17 o 7
