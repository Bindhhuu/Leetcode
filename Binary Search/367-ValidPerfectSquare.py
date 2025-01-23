class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num

        while l<=r:
            m = (l+r)//2
            sq = m*m
            if sq == num:
                return True
            elif sq < num:
                l=m+1
            else:
                
                r= m-1
        return False
