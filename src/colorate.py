
class Colorate:
    def __init__(self, matrix):
        self.matrix = matrix
        #self.initToHex()


    def initToHex(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = hex(self.matrix[i][j])[2:].zfill(6)

    def getMatrix(self):
        return self.matrix