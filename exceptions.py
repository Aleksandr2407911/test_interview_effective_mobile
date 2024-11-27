class IdNotFound(Exception):
    def __init__(self, id, message="ID not found in the database."):
        self.id = id
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (ID: {self.id})"


class SearchParametrsNotEntered(Exception):
    def __init__(self, message="Search paraments are not entered"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.message})"


class BooksWithThisParametrsNotFound(Exception):
    def __init__(self, message="Books with this parametrs are not found"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.message})"


class NoBooksAvailable(Exception):
    def __init__(self, message="No books available"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.message})"


class StatusNotAvailable(Exception):
    def __init__(self, message="Status not available"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.message})"


class BookAlreadyExist(Exception):
    def __init__(self, message="Book is already exist"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.message})"
