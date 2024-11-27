import json
import uuid
from exceptions import (
    IdNotFound,
    SearchParametrsNotEntered,
    BooksWithThisParametrsNotFound,
    NoBooksAvailable,
    StatusNotAvailable,
    BookAlreadyExist,
)
from typing import Optional


class Data_library:
    def __init__(self, data_path):
        self.path_data_file = data_path

    def search_book_by_id(self, id: str) -> tuple[int, list]:
        with open(self.path_data_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            count = 0
            for book in data:
                if book["id"] == id:
                    break
                count += 1
            if count == len(data):
                raise IdNotFound(id)
        return count, data

    def add_book(self, title: str, author: str, year: str) -> str:
        book = {
            "id": str(uuid.uuid4()),
            "title": title,
            "author": author,
            "year": year,
            "status": "В наличии",
        }
        try:
            self.search_book(title, author, year)
        except BooksWithThisParametrsNotFound:
            with open(self.path_data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                data.append(book)

            with open(self.path_data_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return "Книга записна в библиотеку"
        else:
            raise BookAlreadyExist

    def truncate_book(self, id: str) -> str:
        position, data = self.search_book_by_id(id)
        del data[position]

        with open(self.path_data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return "Книга успешно удалена из библиотеки"

    def search_book(
        self,
        title: Optional[str] = None,
        author: Optional[str] = None,
        year: Optional[str] = None,
    ):
        if title == None and author == None and year == None:
            raise SearchParametrsNotEntered()

        with open(self.path_data_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        search_result = []
        for book in data:
            if (
                book["title"] == title
                or book["author"] == author
                or book["year"] == year
            ):
                search_result.append(book)
        if not search_result:
            raise BooksWithThisParametrsNotFound()
        return search_result

    def fetch_all_books(self):
        with open(self.path_data_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not data:
            raise NoBooksAvailable()
        return data

    def change_status(self, book_id: str, new_status: str) -> str:
        if new_status not in ("Выдан", "В наличии"):
            raise StatusNotAvailable()
        position, data = self.search_book_by_id(book_id)

        data[position]["status"] = new_status
        with open(self.path_data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return (
            f"Статус книги {data[position]["title"]} успешно изменен на <{new_status}>"
        )
