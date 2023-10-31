class Solution:
    def isprime(self,n):
        if n<=1:
            return False
        for i in range(2,math.floor(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        l = len(nums[0])
        arr=[]
        for i in range(l):
            arr.append(nums[i][i])
            arr.append(nums[i][l-i-1])
        result=0
        for num in arr:
            if num>result:
                if self.isprime(num):
                    result=num
        return result

'''
Intuition
Iterate through the given matrix, extract the diagonal elements (both main diagonal and anti-diagonal), and check if each element is prime. Finally, return the largest prime number found.

Approach
Define a helper function, isprime(n), to check if a number n is prime.Initialize an empty array arr to store the diagonal elements.
Iterate through the elements in the first row of the given matrix.
Append the element at the current index in both the main diagonal (nums[i][i]) and the anti-diagonal (nums[i][l-i-1]) to arr.
Initialize result to 0, which will store the largest prime number found.
Iterate through the elements in arr.If the current element is greater than result and it is prime (checked using the isprime function), update result to the current element.
Return result.
Complexity
Time complexity:O(n)
Space complexity:O(n) - As we store the diagonal elements in the array.
'''
