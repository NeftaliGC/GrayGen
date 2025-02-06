import numpy as np

class MatrixGenerator:

    matrix = None

    def __init__(self, rows = 400, columns = 400):
        self.rows = rows
        self.columns = columns


    def generateMatrix(self):
        self.matrix = np.random.randint(0, 256, (self.rows, self.columns), dtype=np.uint8)

    def getMatrix(self):
        return self.matrix

    