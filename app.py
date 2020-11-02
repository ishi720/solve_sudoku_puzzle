from flask import Flask, render_template, request, jsonify
import math, json

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
                    checkList = self.checkColumn(checkList, i)

                    """縦のチェック"""
                    checkList = self.checkRow(checkList, j)

                    """3x3のチェック"""
                    checkList = self.checkArea(checkList, i, j)

                    if self.checkNearLine(checkList, i, j):
                        self.puzzle[i][j] = self.checkNearLine(checkList, i, j)

                    if len(checkList) == 1:
                        self.puzzle[i][j] = checkList[0]

    def checkNearLine(self, checkList ,column, row):

        nearColumnList = []
        for i in range(3):
            if column // 3 * 3 + i != column: 
                nearColumnList.append(column // 3 * 3 + i)
        nearColumn1,nearColumn2 = nearColumnList

        nearRowList = []
        for i in range(3):
            if row // 3 * 3 + i != row: 
                nearRowList.append(row // 3 * 3 + i)
        nearRow1,nearRow2 = nearRowList

        work = []
        for x in range(9):
            work.append(self.puzzle[x][nearRow1])
        checkList =  set(checkList) & set(work)

        work = []
        for x in range(9):
            work.append(self.puzzle[x][nearRow2])
        checkList =  set(checkList) & set(work)

        work = []
        for x in range(9):
            work.append(self.puzzle[nearColumn1][x])
        checkList =  set(checkList) & set(work)

        work = []
        for x in range(9):
            work.append(self.puzzle[nearColumn2][x])
        checkList =  set(checkList) & set(work)

        if len(checkList) == 1:
            return list(checkList)[0]
        else:
            return False

    def checkColumn(self, checkList, column):
        """横のチェック"""
        for row in range(9):
            if self.puzzle[column][row] in checkList:
                checkList.remove(self.puzzle[column][row])
        return checkList

    def checkRow(self, checkList, row):
        """縦のチェック"""
        for column in range(9):
            if self.puzzle[column][row] in checkList:
                checkList.remove(self.puzzle[column][row])
        return checkList

    def checkArea(self, checkList, column, row):
        """3x3のエリアのチェック"""
        _column = (column // 3) * 3
        _row = (row // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.puzzle[_column+i][_row+j] in checkList:
                    checkList.remove(self.puzzle[_column+i][_row+j])
        return checkList

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

    # 初級
    # puzzle = [
    #     [0,5,9,0,3,0,7,2,0],
    #     [1,0,7,0,4,0,3,0,8],
    #     [0,6,0,2,0,5,0,4,0],
    #     [3,0,2,1,0,8,5,0,7],
    #     [0,1,0,7,0,6,0,3,0],
    #     [5,0,0,0,0,0,0,0,9],
    #     [0,0,4,0,0,0,6,0,0],
    #     [0,3,0,0,1,0,0,7,0],
    #     [7,0,1,5,6,4,2,0,3]
    # ]

    # 中級
    puzzle = [
        [8,0,0,0,0,0,0,0,3],
        [0,0,0,0,4,0,0,0,0],
        [5,0,0,1,9,6,0,0,7],
        [9,0,6,2,0,4,3,0,1],
        [0,7,0,0,0,0,0,6,0],
        [1,0,8,3,0,7,9,0,4],
        [3,0,0,4,7,2,0,0,9],
        [0,0,0,0,5,0,0,0,0],
        [2,0,0,0,0,0,0,0,6]
    ]

    # 上級
    # puzzle = [
    #     [3,0,6,0,0,0,4,0,5],
    #     [0,0,0,0,8,0,0,0,0],
    #     [0,0,0,6,0,2,0,0,0],
    #     [1,4,2,0,0,0,9,8,3],
    #     [0,0,7,4,0,1,2,0,0],
    #     [6,5,9,0,0,0,1,4,7],
    #     [0,0,0,9,0,7,0,0,0],
    #     [0,0,0,0,1,0,0,0,0],
    #     [2,0,5,0,0,0,7,0,8]
    # ]

    puzzleObj = SudokuPuzzle(puzzle)
    percentage,fraction = puzzleObj.progress()

    return render_template(
        'index.html',
        title='Solve Sudoku Puzzle',
        puzzle=puzzle,
        percentage= str(percentage) + '%',
        fraction= "(" + str(fraction) + ")"
    )

@app.route('/api/', methods=['POST'])
def index():
    puzzle = json.loads(request.form['puzzle'])
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