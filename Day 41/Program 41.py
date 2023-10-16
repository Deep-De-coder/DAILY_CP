# Intuition
# First think about it like this, that they need to minimize the costs of the chocolates and want to select two of them, so the most simple way of going about it can be selecting the minimum and the second minimum cost chocolates.

# Approach
# To approach this, that is what i did in the code. I found out the minimum cost chocolate and added it to the predicted money spent. Then, I removed that cost from the prices array and looked for the next minimum cost(here the cost can be same as the first chocolate cost or less than that). Add it to the spent variable as well and then check if the spent is less than or equal to money given (that's how you get a non negative amount to return)

# Complexity
# Time complexity: O(n)
# Space complexity: O(1)
# Code
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = min(prices)
        spent = first
        prices.remove(first)
        second = min(prices)
        spent+=second
        if spent<=money:
            return money - spent
        else:
            return money
