### LC Problem
### Difficulty Easy
### 1672. Check If It Is a Straight Line
### https://leetcode.com/problems/richest-customer-wealth/

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        x = len(accounts)
        z = 0
        sumlist = []
        for i in range(x):
            for j in range(len(accounts[i])):
                z += accounts[i][j]
            sumlist.append(z)
            z=0
        return max(sumlist)

accounts = [[1,2,3],[3,2,1]]
solution = Solution()
print(solution.maximumWealth(accounts))