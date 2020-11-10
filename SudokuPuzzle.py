import math

class SudokuPuzzle:
    puzzle = []
    candidate = []

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.candidate = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]
        self.candidateCheck()

    def solver(self):
        for i in range(9):
            for j in range(9):
                checkList = [1,2,3,4,5,6,7,8,9]
                if self.puzzle[i][j] == 0:
                    """横のチェック"""
                    checkList = self.checkColumn(checkList, i)

                    """縦のチェック"""
                    checkList = self.checkRow(checkList, j)

                    """3x3のチェック"""
                    checkList = self.checkArea(checkList, i, j)

                    if self.checkNearLine(checkList, i, j):
                        self.puzzle[i][j] = self.checkNearLine(checkList, i, j)

                        self.rowCandidateRemove(i, self.puzzle[i][j])
                        self.columnCandidateRemove(j, self.puzzle[i][j])
                        self.areaCandidateRemove(i, j, self.puzzle[i][j])

                    if len(checkList) == 1:
                        self.puzzle[i][j] = checkList[0]

                        self.rowCandidateRemove(i, self.puzzle[i][j])
                        self.columnCandidateRemove(j, self.puzzle[i][j])
                        self.areaCandidateRemove(i, j, self.puzzle[i][j])

                    """候補のチェック"""
                    self.checkCandidate(i, j)

    def candidateCheck(self):
        for i in range(9):
            for j in range(9):
                checkList = [1,2,3,4,5,6,7,8,9]
                if self.puzzle[i][j] == 0:
                    """横のチェック"""
                    checkList = self.checkColumn(checkList, i)

                    """縦のチェック"""
                    checkList = self.checkRow(checkList, j)

                    """3x3のチェック"""
                    checkList = self.checkArea(checkList, i, j)

                    self.candidate[i][j] = checkList
                else:
                    self.candidate[i][j] = [self.puzzle[i][j]]

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

    def checkCandidate(self, row, column):

        # 確定済みのマスはスキップする
        if self.puzzle[row][column] != 0:
            return

        # 縦の候補をまとめる
        work = []
        for i in range(9):
            if i == row:
                continue
            if self.puzzle[i][column] == 0:
                work += self.candidate[i][column]

        # チェックマスにしかない候補をセットする
        for n in self.candidate[row][column]:
            if n not in work:
                self.puzzle[row][column] = n
                self.candidate[row][column] = [n]

                # 確定したら関連するマスから候補を削除する
                self.rowCandidateRemove(row, n)
                self.areaCandidateRemove(row, column, n)

        work = []
        for j in range(9):
            if j == column:
                continue
            if self.puzzle[row][j] == 0:
                work += self.candidate[row][j]

        # チェックマスにしかない候補をセットする
        for n in self.candidate[row][column]:
            if n not in work:
                self.puzzle[row][column] = n
                self.candidate[row][column] = [n]

                # 確定したら関連するマスから候補を削除する
                self.columnCandidateRemove(column, n)
                self.areaCandidateRemove(row, column, n)

        work = []
        _row = (row // 3) * 3
        _column = (column // 3) * 3
        for i in range(3):
            for j in range(3):
                if i == _row and j == _column:
                    continue
                if self.puzzle[_row+i][_column+j] == 0:
                    work += self.candidate[_row+i][_column+j]

        # チェックマスにしかない候補をセットする
        for n in self.candidate[row][column]:
            if n not in work:
                self.puzzle[row][column] = n
                self.candidate[row][column] = [n]

                # 確定したら関連するマスから候補を削除する
                self.columnCandidateRemove(column, n)
                self.rowCandidateRemove(row, n)


    def columnCandidateRemove(self, column, candidateNum):
        for i in range(9):
            if len(self.candidate[i][column]) != 1:
                if candidateNum in self.candidate[i][column]:
                    self.candidate[i][column].remove(candidateNum)

    def rowCandidateRemove(self, row, candidateNum):
        for j in range(9):
            if len(self.candidate[row][j]) != 1:
                if candidateNum in self.candidate[row][j]:
                    self.candidate[row][j].remove(candidateNum)

    def areaCandidateRemove(self, row, column, candidateNum):
        _row = (row // 3) * 3
        _column = (column // 3) * 3
        for i in range(3):
            for j in range(3):
                if len(self.candidate[_row+i][_column+j]) != 1:
                    if candidateNum in self.candidate[_row+i][_column+j]:
                        self.candidate[_row+i][_column+j].remove(candidateNum)