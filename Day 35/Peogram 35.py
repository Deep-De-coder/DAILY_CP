class Solution:
    def distanceTraveled(self, mainTank, additionalTank):
        sum = 0
        x = 0
        y = 0
        while mainTank >= 5:
            x = mainTank // 5
            y = mainTank % 5
            if additionalTank >= x:
                mainTank = y + x
            elif additionalTank >= 0:
                mainTank = y + additionalTank
            else:
                mainTank = y
            additionalTank = additionalTank - x
            sum = sum + x * 5 * 10
        return sum + mainTank * 10

  '''
  Intuition
Brute-force

Approach
x here represents the total possible km factors. For example, if the maintank is 26, then x will be 5, which means we will require additionalTank 5 times.
y represents the remaining fuel after dividing 5 times. This means we will later add y to additionalTank.
If additionalTank is more than x, it means there is extra fuel in additionalTank, so we will only use x from additionalTank.
Else if additionalTank is less than x, we will use all of the additionalTank.
Otherwise, we will update mainTank by y, which is the remaining fuel in the main tank. (Use this test case to understand: maintank=19 and additionaltank=1)
Then, we will subtract additionalTank by x.
After that, we will calculate the sum by adding x * 5 * 10.
If any fuel remains, we will return it by using the fuel from the maintank as well.
'''
