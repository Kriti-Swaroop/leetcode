#THIS CODE IS RELATED TO PROBLEM 2054. Two Best Non-Overlapping Events IN LEETCODE
#BELOW IS THE PROBLEM STATEMENT FOR REFERENCE
#TOPIC: HEAP(PRIORITY QUEUE)

'''You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, 
and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is 
maximized.
Return this maximum sum.'''

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        pq = [] #stores (end_time, value)
        maxx = 0
        res = 0
        for start, end, value in events:
            while pq and pq[0][0] < start: #remember pq[i][0] will have end_time
                maxx = max(maxx, heapq.heappop(pq)[1]) #finding max value in pq
            res = max(res, maxx + value)
            heapq.heappush(pq, (end, value))
        return res
