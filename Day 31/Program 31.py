class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triplet = [nums[i], nums[l], nums[r]]
                    answer.append(triplet)
                    while l < r and nums[l] == triplet[1]:
                        l += 1
                    while l < r and nums[r] == triplet[2]:
                        r -= 1
        return answer

'''
This problem is similar to Two Sum, but the main differentiator is that there can now be multiple solutions and we must not return duplicate ones. This requires us to use a different approach, since Two Sum assumes that there is only one solution.

The key is to sort the array first. We then use an outer loop to fix one of the numbers and use a two pointer approach to find all solutions for that number. The pointers, l and r, start at the ends of the array and work themselves inwards.

At each iteration, we calculate the total and compare it to 0. If the total is less than zero, then since we need to make the total larger and the array is sorted, the only thing we can do is move l up (moving r down would only make the total smaller). Similarly, if the total is greater than 0, then we just move r down.

If the total is equal to 0, then that means we've found a solution, so we append the triplet to our answer array and then keep moving l and r inwards until they both get to different numbers.

Youtube :https://youtu.be/IIxoo93bmPQ 
'''
