class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        count=Counter(ranks)
        left=1
        right=min(count)*cars*cars
        while left<right:
            mid=(left+right)//2
            if sum(isqrt(mid//a)*count[a] for a in count)<cars:
                left=mid+1

            else:
                right=mid

        return left            
