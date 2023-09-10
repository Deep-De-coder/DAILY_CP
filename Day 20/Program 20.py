class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        res = -1
        data = collections.defaultdict(list)

        for value in nums :
            data[max([x for x in str(value)])].append(value)

        for value in data.values() :
            if len(value) > 1 :
                value.sort()
                tmp = value.pop()+value.pop()
                if tmp > res : res = tmp

        return res
'''
Intuition
Record the maximum digit of each number in the nums list as the key in a dictionary, with the number itself as the value.

Finally, iterate through the dictionary, add the two largest values for each key, and find the maximum among all the answers.

Approach
The ability to compare each number's maximum digit using the comparison features of strings in Python.

We will use collections.defaultdict(list) for the purpose of conveniently grouping numbers with the same maximum digit into the same array.

Complexity
Time complexity:
O(N + k + MlogM),
N is the length of the nums list,
k is the maximum number of digits in any number,
M is the total count of numbers with the same leading digit.

Space complexity:
O(N) due to the data dictionary.
'''
