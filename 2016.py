#THIS CODE IS RELATED TO PROBLEM 2016. Maximum Difference Between Increasing Elements IN LEETCODE
#BELOW IS THE PROBLEM STATEMENT FOR REFERENCE
#TOPIC: ARRAY

'''Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
Return the maximum difference. If no such i and j exists, return -1.'''

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = -1
        mini = nums[0]
        for i in range(1, len(nums)):
            mini = min(mini, nums[i])
            if nums[i] > mini:
                diff = max(diff, nums[i]-mini)
        return diff
        '''mini = nums.index(min(nums))
        left = nums[mini+1:]
        print(mini, left)
        if not left:
            return -1
        maxi = left.index(max(left))
        print(maxi)
        return nums[maxi+mini+1]-nums[mini] #bcoz maxi is index of leftover list, so need to add '''
