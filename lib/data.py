

class DataSteam:
    """"""
    def __init__(self, file=None):
        self.file = file
        self.contents = ""
        with open(self.file, 'r') as f:
            self.contents = f.read()






