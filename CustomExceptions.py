class CustomExceptions(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ExceptionSaveFields(CustomExceptions):
    pass
