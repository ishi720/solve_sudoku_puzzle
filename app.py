from flask import Flask, render_template, request, jsonify
import json
from module import SudokuPuzzle

app = Flask(__name__)

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
    # puzzle = [
    #     [8,0,0,0,0,0,0,0,3],
    #     [0,0,0,0,4,0,0,0,0],
    #     [5,0,0,1,9,6,0,0,7],
    #     [9,0,6,2,0,4,3,0,1],
    #     [0,7,0,0,0,0,0,6,0],
    #     [1,0,8,3,0,7,9,0,4],
    #     [3,0,0,4,7,2,0,0,9],
    #     [0,0,0,0,5,0,0,0,0],
    #     [2,0,0,0,0,0,0,0,6]
    # ]

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

    # 最上級
    puzzle = [
        [0,0,2,0,4,0,8,0,0],
        [0,0,0,9,0,7,0,0,0],
        [0,7,0,0,2,0,0,4,0],
        [0,0,4,0,6,0,1,0,0],
        [6,0,7,1,0,2,4,0,5],
        [0,0,9,0,7,0,6,0,0],
        [0,8,0,0,1,0,0,3,0],
        [0,0,0,2,0,4,0,0,0],
        [0,0,1,0,9,0,2,0,0]
    ]

    puzzleObj = SudokuPuzzle.SudokuPuzzle(puzzle)
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
    puzzleObj = SudokuPuzzle.SudokuPuzzle(puzzle)
    puzzleObj.solveTheEnd()
    percentage,fraction = puzzleObj.progress()
    checkCount = puzzleObj.checkCount

    return jsonify({
        'percentage': percentage,
        'fraction': fraction,
        'afterPuzzle': puzzleObj.puzzle,
        'checkCount': checkCount
    })

if __name__ == "__main__":
    app.run(debug=True)