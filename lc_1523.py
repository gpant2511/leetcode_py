### LC Problem
### Difficulty Easy
### 1523. Count Odd Numbers in an Interval Range
### https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a=high-low+1
        if(low%2!=0 and high%2!=0):
            b=a//2+1
        else:
            b=a//2
        
        return(b)

solution = Solution()
print(solution.countOdds(3, 7))
print(solution.countOdds(8, 10))
print(solution.countOdds(1, 10))
