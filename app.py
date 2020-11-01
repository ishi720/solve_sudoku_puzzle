from flask import Flask, render_template, jsonify
import math
app = Flask(__name__)

class SudokuPuzzle:
    puzzle = []

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solver(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    checkList = [1,2,3,4,5,6,7,8,9]

                    """横のチェック"""
                    if self.puzzle[i][0] in checkList:
                        checkList.remove(self.puzzle[i][0])
                    if self.puzzle[i][1] in checkList:
                        checkList.remove(self.puzzle[i][1])
                    if self.puzzle[i][2] in checkList:
                        checkList.remove(self.puzzle[i][2])
                    if self.puzzle[i][3] in checkList:
                        checkList.remove(self.puzzle[i][3])
                    if self.puzzle[i][4] in checkList:
                        checkList.remove(self.puzzle[i][4])
                    if self.puzzle[i][5] in checkList:
                        checkList.remove(self.puzzle[i][5])
                    if self.puzzle[i][6] in checkList:
                        checkList.remove(self.puzzle[i][6])
                    if self.puzzle[i][7] in checkList:
                        checkList.remove(self.puzzle[i][7])
                    if self.puzzle[i][8] in checkList:
                        checkList.remove(self.puzzle[i][8])

                    """縦のチェック"""
                    if self.puzzle[0][j] in checkList:
                        checkList.remove(self.puzzle[0][j])
                    if self.puzzle[1][j] in checkList:
                        checkList.remove(self.puzzle[1][j])
                    if self.puzzle[2][j] in checkList:
                        checkList.remove(self.puzzle[2][j])
                    if self.puzzle[3][j] in checkList:
                        checkList.remove(self.puzzle[3][j])
                    if self.puzzle[4][j] in checkList:
                        checkList.remove(self.puzzle[4][j])
                    if self.puzzle[5][j] in checkList:
                        checkList.remove(self.puzzle[5][j])
                    if self.puzzle[6][j] in checkList:
                        checkList.remove(self.puzzle[6][j])
                    if self.puzzle[7][j] in checkList:
                        checkList.remove(self.puzzle[7][j])
                    if self.puzzle[8][j] in checkList:
                        checkList.remove(self.puzzle[8][j])

                    """9x9のチェック"""
                    _i = (i // 3) * 3
                    _j = (j // 3) * 3
                    if self.puzzle[_i][_j] in checkList:
                        checkList.remove(self.puzzle[_i][_j])
                    if self.puzzle[_i+1][_j] in checkList:
                        checkList.remove(self.puzzle[_i+1][_j])
                    if self.puzzle[_i+2][_j] in checkList:
                        checkList.remove(self.puzzle[_i+2][_j])
                    if self.puzzle[_i][_j+1] in checkList:
                        checkList.remove(self.puzzle[_i][_j+1])
                    if self.puzzle[_i+1][_j+1] in checkList:
                        checkList.remove(self.puzzle[_i+1][_j+1])
                    if self.puzzle[_i+2][_j+1] in checkList:
                        checkList.remove(self.puzzle[_i+2][_j+1])
                    if self.puzzle[_i][_j+2] in checkList:
                        checkList.remove(self.puzzle[_i][_j+2])
                    if self.puzzle[_i+1][_j+2] in checkList:
                        checkList.remove(self.puzzle[_i+1][_j+2])
                    if self.puzzle[_i+2][_j+2] in checkList:
                        checkList.remove(self.puzzle[_i+2][_j+2])

                    if len(checkList) == 1:
                        self.puzzle[i][j] = checkList[0]


    def progress(self):
        """進捗率の計算"""
        counter = 0
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] != 0:
                    counter += 1
        return math.floor(counter / 81 * 100), str(counter) + '/81'



@app.route('/')
def hello():
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

    return render_template('index.html', title='test', puzzle=puzzle)

@app.route('/api/')
def index():
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
    puzzleObj = SudokuPuzzle(puzzle)
    puzzleObj.solver()
    percentage,fraction = puzzleObj.progress()

    return jsonify({
        'percentage': percentage,
        'fraction': fraction,
        'afterPuzzle': puzzleObj.puzzle
    })

if __name__ == "__main__":
    app.run(debug=True)