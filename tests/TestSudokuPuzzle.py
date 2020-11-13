from unittest import TestCase
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from module.SudokuPuzzle import SudokuPuzzle

class TestSudokuPuzzle(TestCase):

    def test_puzzle1(self):
        """初級問題のテスト"""
        puzzle = [
            [0,5,9,0,3,0,7,2,0],
            [1,0,7,0,4,0,3,0,8],
            [0,6,0,2,0,5,0,4,0],
            [3,0,2,1,0,8,5,0,7],
            [0,1,0,7,0,6,0,3,0],
            [5,0,0,0,0,0,0,0,9],
            [0,0,4,0,0,0,6,0,0],
            [0,3,0,0,1,0,0,7,0],
            [7,0,1,5,6,4,2,0,3]
        ]
        answer = [
            [4,5,9,8,3,1,7,2,6],
            [1,2,7,6,4,9,3,5,8],
            [8,6,3,2,7,5,9,4,1],
            [3,4,2,1,9,8,5,6,7],
            [9,1,8,7,5,6,4,3,2],
            [5,7,6,4,2,3,1,8,9],
            [2,9,4,3,8,7,6,1,5],
            [6,3,5,9,1,2,8,7,4],
            [7,8,1,5,6,4,2,9,3]
        ]
        puzzleObj = SudokuPuzzle(puzzle)
        puzzleObj.solveTheEnd()
        self.assertEqual(puzzleObj.puzzle, answer)

if __name__ == "__main__":
    unittest.main()