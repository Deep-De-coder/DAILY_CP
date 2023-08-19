class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)




'''Intuition and Approach
We can climb nnn stairs by going up 1 or 2 steps at a time. So if we're currently on step iii, the only places we could get to in one iteration would be steps i+1i + 1i+1 (if we take 1 step) and i+2i + 2i+2 (if we take 2 steps).

This means that if we are currently on step nnn, our final destination, we could have only gotten there in one of two ways:

From step n−1n - 1n−1 , having gone up 1 step to nnn
From step n−2n - 2n−2, having gone up 2 steps to nnn
This highlights that the number of ways to reach step nnn depends on the number of ways to get to step n−1n - 1n−1 and the number of ways to get to step n−2n - 2n−2. Since both of the above possibilities are valid choices, the number of ways to get to nnn is going to be their sum. Thus, we have the following relationship (formally called a recurrence relation): ways(n)=ways(n−1)+ways(n−2)ways(n) = ways(n - 1) + ways(n - 2)ways(n)=ways(n−1)+ways(n−2)

Looking at the problem constraints, we see that the smallest possible value of nnn is 1. If we are asked to climb 1 step, the above relationship will not work because ways(0)ways(0)ways(0) and ways(−1)ways(-1)ways(−1) are not defined. More formally, we haven't defined our recurrence's base case(s). We calculate this base case manually: there's only 1 way to climb a singular step - just climb that step! We couldn't possibly take 2 steps in this situation, because then we'd be climbing more steps than there are to climb. We notice that if n=2n = 2n=2, the relationship will also not hold because ways(0)ways(0)ways(0) is still undefined. Calculating this base case is slightly more involved, but still easy: we can either climb the 2 steps by taking 2 steps, or climb 1 step twice, for a total of 2 ways to climb.

To recap, we have the following relationship, depending on the value of nnn:

ways(1)=1 for n=1ways(1) = 1 \text{ for } n = 1ways(1)=1 for n=1
ways(2)=2 for n=2ways(2) = 2 \text{ for } n = 2ways(2)=2 for n=2
ways(n)=ways(n−1)+ways(n−2) for n>2ways(n) = ways(n - 1) + ways(n - 2) \text{ for } n > 2ways(n)=ways(n−1)+ways(n−2) for n>2
Implementation
We'll explore multiple approaches from simple to more complex, incrementally improving upon each solution.

1. Naive recursion
We can translate the recurrence we came up with earlier into code, as follows:

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
However, running this yields Time Limit Exceeded. Why is it so inefficient? Let's think about calculating the ways to climb 6 stairs, climbStairs(6).

                                       climbStairs(6)
									 /               \
								cS(5)       +          cS(4)
					           /    \                  /    \
			               cS(4)   +   cS(3)         cS(3) + cS(2)
						   /  \        /   \         /   \
				      cS(3) + cS(2) cS(2) + cS(1) cS(2) + cS(1)
					  /  \
			     cS(2) + cS(1)
			
	
As you can see from the recursion tree above, we are calculating climbStairs(4) and climbStairs(3) multiple times. Specifically, climbStairs(4) is being recalculated twice, while climbStairs(3) is being recalculated 3 times. If you think about what happens for larger values of n, you can see that we are recalculating a lot of values!

Complexity

Time: Each additional level in the recursion tree is going to have double the amount of calls to climbingStairs than the one above it. For nnn, this gives us a staggering 2n2^n2 
n
  function calls, for a O(2n)O(2^n)O(2 
n
 ) time complexity. No wonder we get TLE!
Space: We aren't storing any additional variables, so that's a O(1)O(1)O(1) space complexity.
Can we avoid repeated computation?

2. Memoization (Top-Down DP)
What if instead of recomputing each value of climbStairs, we made sure to save the unique values (such as climbingStairs(5)), trading space for time? That's what a top-down dynamic programming approach called memoization is. We make use of a dictionary memo in which we store the values of climbStairs that we have computed, and if we ever have to compute that value again we just check memo in (average) O(1)O(1)O(1) time instead of doing the work all over again.

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):  # inner function to make code simpler
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n-1) + climb(n-2)
                return memo[n]
        memo = {1: 1, 2: 2}  # base cases
        return climb(n)
We can also make use of Python's handy @cache function decorator that does this for us in the background like so:

class Solution:
	@cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
This top-down paradigm works well when we approach the problem from the top of the stairs (the last step we needed to climb, nnn) down.

Complexity

Time: There are O(n)O(n)O(n) distinct subproblems to solve, each requiring only O(1)O(1)O(1) amount of work of getting the values of smaller subproblems from memo and adding them together. When we encounter a subproblem we've already solved, we can get the answer in O(1)O(1)O(1) time.
Space: We are using an additional memo dictionary that will store the answer to each subproblem, so O(n)O(n)O(n) space complexity.
Can we be even more efficient and avoid the overhead of recursion?

3. Bottom-Up DP
Turns out we can build the solution from the ground up (quite literally in this case). From our recurrence relation, we saw that the number of ways to climb nnn stairs depends on the number of ways to climb n−1n - 1n−1 and n−2n - 2n−2 stairs. So instead of approaching the problem top-down and computing these values recursively, we compute them bottom-up, starting with the base cases and building upon the previous values until we reach nnn. We use a dp array of length n+1n + 1n+1 (to accomodate for the 0-based indexing of Python; we could just have it be length nnn and return dp[n - 1] but in this way we are aligning the step numbers with the indices) and successively build up each index from the previous two.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [-1] * (n + 1)  # to accomodate for 0-based indexing 
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
            
Complexity

Time: As before, we are computing each subproblem once and each subproblem requires constant amount of work (just the addition of the previous 2 elements of the array). That's O(n)O(n)O(n)time complexity.
Space: Since we are storing the answers to previous subproblems in the dp array, this will be O(n)O(n)O(n) too.
Can we do even better?

4. Optimizied Bottom-Up DP
While the above works well enough, we can optimize our approach even further by making a simple but important observation: we are only utilizing the last 2 subproblem answers when solving each subproblem. If you look at the recurrence again, you can see that the only pieces information we use are ways(n−1)ways(n - 1)ways(n−1) and ways(n−2)ways(n - 2)ways(n−2). Since we're computing from bottom-up, once we compute those answers, the smaller subproblems (such as ways(n−3)ways(n - 3)ways(n−3)) are not needed anymore. Thus, instead of keeping the entire dp array, we can save some space and just maintain 2 variables that track our last 2 subproblem answers!

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ways = 0
		# base cases
        two_below_curr = 1  # 2 steps below 3 - ways to take 1 step: 1
        one_below_curr = 2  # 1 step below 3 - ways to take 2 steps: 2
        for i in range(3, n + 1):
            # compute number of ways for i
            ways = one_below_curr + two_below_curr
            # step up to i + 1   
            # 1 step below becomes 2 steps below
            # current number of ways becomes 1 step below
            two_below_curr, one_below_curr = one_below_curr, ways
    
        return ways
Complexity

Time: As before, we are computing each subproblem once and each subproblem requires constant amount of work (just the addition of the previous 2 number of ways). That's O(n)O(n)O(n) time complexity.
Space: O(1)O(1)O(1) since we are maintaining 3 extra variables only!
And that's it! We went from a TLE solution to an elegant and optimized version.
'''
