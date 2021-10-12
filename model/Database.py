class Database:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __str__(self):
        return self.name
