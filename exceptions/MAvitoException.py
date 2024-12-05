class MAvitoException(Exception):
    def __init__(self, error_message):
        self.__error_message = error_message

    def what(self):
        return self.__error_message
