### LC Problem
### Difficulty Easy
### 1672. Check If It Is a Straight Line
### https://leetcode.com/problems/richest-customer-wealth/

from typing import List
import unittest

class Solution:
    def maximumWealth_optimal(self, accounts: List[List[int]]) -> int:
        return 0
    
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

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def test_maximumWealth_1(self):
        accounts = [[1,2,3],[3,2,1]]
        self.assertEqual(self.solution.maximumWealth(accounts), 6)

    def test_maximumWealth_2(self):
        accounts = [[1,5],[7,3],[3,5]]
        self.assertEqual(self.solution.maximumWealth(accounts), 10)
    
if __name__ == '__main__':
    unittest.main()
