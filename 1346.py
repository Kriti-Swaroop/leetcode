#THIS CODE IS RELATED TO PROBLEM 1346. Check If N and Its Double Exist IN LEETCODE
#BELOW IS THE PROBLEM STATEMENT FOR REFERENCE
#TOPIC: ARRAY

'''Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]'''

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        prev=[]
        for i in arr:
            print(i, i*2, i//2)
            if i * 2 in prev or (i%2==0 and i // 2 in prev):
                return True
            else:
                print(i)
                prev.append(i)
        return False
