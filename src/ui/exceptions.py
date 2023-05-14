class IDFoundException(Exception):
    def __init__(self, id):
        super().__init__()
        self._id = id

    def __str__(self):
        return f"! ! ! ID already in use! Your input: {self._id}"
class IDInvalidException(Exception):
    def __init__(self, id):
        super().__init__()
        self._id = id

    def __str__(self):
        return f"! ! ! ID must be a nonzero integer! Your input: {self._id}"

class GradeException(Exception):
    def __init__(self, id):
        super().__init__()
        self._id = id

    def __str__(self):
        return f"! ! ! Grade must be an integer between 1 and 10! Your input: {self._id}"
class IDNotFoundException(Exception):
    def __init__(self, id):
        super().__init__()
        self._id = id

    def __str__(self):
        return f"! ! ! ID not found! Your input: {self._id}"