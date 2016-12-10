from random import gauss

class ClimbingGame:
    def __init__(self, caseNr):
        self.matrix = [0]*3
        for i in range(len(self.matrix)):
            self.matrix[i] = [0]*3
        if caseNr == 0:
            self.sigma, self.sigma0, self.sigma1 = 0.2, 0.2, 0.2
        elif caseNr == 1:
            self.sigma, self.sigma1 = 0.1, 0.1
            self.sigma0 = 4
        elif caseNr == 2:
            self.sigma, self.sigma0 = 0.1, 0.1
            self.sigma1 = 4

    def get(self,i, j):
        if i==0 and j==0:
            return gauss(11, self.sigma0**2)
        elif i==0 and j==1:
            return gauss(-30, self.sigma**2)
        elif i==0 and j==2:
            return gauss(0, self.sigma**2)

        elif i==1 and j==0:
            return gauss(-30, self.sigma**2)
        elif i==1 and j==1:
            return gauss(7, self.sigma1**2)
        elif i==1 and j==2:
            return gauss(6, self.sigma**2)

        elif i==2 and j==0:
            return gauss(0, self.sigma**2)
        elif i==2 and j==1:
            return gauss(0, self.sigma**2)
        elif i==2 and j==2:
            return gauss(5, self.sigma**2)

