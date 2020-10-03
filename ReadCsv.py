class ReadCsv():

    def readCsv(self,pathOfCsv):
        output = []
        csvFile = open(pathOfCsv, newline='',encoding="utf-8")
        for line in csvFile:
            row = [line]
            output.append(row)
        return output