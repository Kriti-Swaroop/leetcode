#THIS CODE IS RELATED TO PROBLEM 1652. DEFUSE THE BOMB IN LEETCODE
#BELOW IS THE PROBLEM STATEMENT FOR REFERENCE
#TOPIC: SLIDING WINDOW

'''You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!'''

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)

        n=len(code)
        res=[0]*n
        if k>0:
            res[0]=win_sum=sum(code[1:k+1])
            for left in range(1,n):
                right=(left+k)%n
                win_sum+= -code[left]+code[right] #removing double code[i]
                res[left]=win_sum
            return res
        res[0]=win_sum=sum(code[-1:k-1:-1])
        for right in range(1,n):
            left=(right-k)%n
            win_sum+= -code[-right]+code[-left]
            res[-right]=win_sum
        return res
