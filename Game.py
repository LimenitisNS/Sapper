import random

class Game(object):

    def __init__(self, rows = 10, cols = 10, mines = 20):

        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.cell = Cell(rows, cols)
        self.playerCell = {}
        self.score = 0
        self.gameOver = False


    def GameStart(self):

        Game.__SetMines(self)
        Game.__SetPlayerCell(self)
        Game.__Start(self)
        
    def __SetMines(self):

        randomNum = 0
        placedMines = 0

        while(placedMines != self.mines):
            for numRows in range(self.rows):
                for numCols in range(self.cols):
                    if(placedMines == self.mines):
                        return

                    randomNum = random.randint(1, 100)

                    if(randomNum >= 90 and self.cell.cell[numRows, numCols] == False):
                        self.cell.cell[numRows, numCols] = True
                        placedMines += 1
                    

    def __SetPlayerCell(self):

        for numRows in range(self.rows):
            for numCols in range(self.cols):
                self.playerCell[numRows, numCols] = '#'
    

    def __Start(self):

        choiceRow = self.rows
        choiceCol = self.cols

        while(True):

            Game.__PrintPlayerCell(self)

            while((choiceRow >= self.rows) or (choiceCol >= self.cols)):
                print("Selected row: ")
                choiceRow = int(input())

                print("Selected col: ")
                choiceCol = int(input())

            while((self.playerCell[choiceRow - 1, choiceCol - 1] != '#')):

                print("Selected row: ")
                choiceRow = int(input())

                print("Selected col: ")
                choiceCol = int(input())

            if(choiceRow != 0 and choiceCol != 0):
                if(self.cell.cell[choiceRow - 1, choiceCol - 1] == True):
                    print("\n\n\nBYM | GAME OVER | BYM | GAME OVER | BYM | GAME OVER | BYM\n")
                    self.gameOver = True
                    Game.__GameOver(self)
                    Game.__PrintPlayerCell(self)
                    return
                else:
                    Game.__OpenFieldCell(self, choiceRow - 1, choiceCol - 1)

            print("____________________________________________")

            choiceRow = self.rows
            choiceCol = self.cols


    def __PrintPlayerCell(self):

        print("\n")
        print("\t", end ="")

        for numCols in range(self.cols):
            print(f"{numCols + 1}", end=" ")
        print("\n\n")

        print("\t", end =" ")
        for numCols in range(self.cols):
            print("_", end=" ")
        print()

        for numRows in range(self.rows):
            print(f"{numRows + 1}", end="\t|")
            print(*[self.playerCell[numRows, numCols] for numCols in range(self.cols)])

        print("\n")


    def __OpenFieldCell(self, choiceRow, choiceCol):

        numberMines = 0

        motions = { (-1, 0): [-1, 0],
                    (-1, 1): [-1, 1],
                    (0, 1): [0, 1],
                    (1, 1): [1, 1],
                    (1, 0): [1, 0],
                    (1, -1): [1, -1],
                    (0, -1): [0, -1],
                    (-1, -1): [-1, -1]
                  }

        for motion in motions:
            try:
                if(self.cell.cell[choiceRow + motions[motion][0], choiceCol + motions[motion][1]] == True):
                    numberMines += 1
            except:
                numberMines = numberMines

        self.playerCell[choiceRow, choiceCol] = numberMines

        if(self.gameOver == False):
            self.score += numberMines
        

    def __GameOver(self):

        for numRow in range(self.rows):
            for numCol in range(self.cols):
                if (self.cell.cell[numRow, numCol] == True):
                    self.playerCell[numRow, numCol] = "b"
                else:
                    Game.__OpenFieldCell(self, numRow, numCol)

        print(f"\nYOUR SCORE:{self.score}")

class Cell:

    def __init__(self, rows, cols):
        cell = {}

        for numRows in range(rows):
            for numCols in range(cols):
                cell[numRows, numCols] = False

        self.cell = cell
