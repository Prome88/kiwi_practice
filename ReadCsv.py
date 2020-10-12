class ReadCsv():

    def read_csv(self, path_of_csv):
        output = []
        csv_file = open(path_of_csv, newline='',encoding="utf-8")
        for line in csv_file:
            row = [line]
            output.append(row)
        return output
