### LC Problem
### Difficulty Easy
### 1232. Check If It Is a Straight Line
### https://leetcode.com/problems/check-if-it-is-a-straight-line/

from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x = len(coordinates)
        s = set()
        for i in range(x-1):
            m = 2**31
            if (coordinates[i+1][0]-coordinates[i][0]) != 0:
                m = (coordinates[i+1][1]-coordinates[i][1])/(coordinates[i+1][0]-coordinates[i][0])
            s.add(m)
        if len(s)==1:
            return True
        return False


t1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
t2 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
solution = Solution()
print(solution.checkStraightLine(t1))
print(solution.checkStraightLine(t2))
