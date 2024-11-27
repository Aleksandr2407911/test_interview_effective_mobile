import pytest
from main import Data_library
import json
import os
from exceptions import IdNotFound

file_path = "./test_data.json"

test_data = [
    {
        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "title": "Мастер и Маргарита",
        "author": "Булгаков",
        "year": "1967",
        "status": "Выдан",
    },
    {
        "id": "b2c3d4e5-f6g7-8901-bcde-f23456789012",
        "title": "1984",
        "author": "Джордж Оруэлл",
        "year": "1949",
        "status": "Выдан",
    },
    {
        "id": "c3d4e5f6-g7h8-9012-cdef-g34567890123",
        "title": "Убить пересмешника",
        "author": "Харпер Ли",
        "year": "1960",
        "status": "Выдан",
    },
    {
        "id": "d4e5f6g7-h8i9-0123-defg-h45678901234",
        "title": "Гордость и предубеждение",
        "author": "Джейн Остин",
        "year": "1813",
        "status": "Выдан",
    },
    {
        "id": "e5f6g7h8-i9j0-1234-efgh-i56789012345",
        "title": "Великий Гэтсби",
        "author": "Фрэнсис Скотт Фицджеральд",
        "year": "1925",
        "status": "Выдан",
    },
    {
        "id": "f6g7h8i9-j0k1-2345-fghi-j67890123456",
        "title": "Преступление и наказание",
        "author": "Достоевский",
        "year": "1866",
        "status": "В наличии",
    },
    {
        "id": "g7h8i9j0-k1l2-3456-ghij-k78901234567",
        "title": "Старик и море",
        "author": "Эрнест Хемингуэй",
        "year": "1952",
        "status": "В наличии",
    },
    {
        "id": "h8i9j0k1-l2m3-4567-hijk-l89012345678",
        "title": "451 градус по Фаренгейту",
        "author": "Рэй Брэдбери",
        "year": "1953",
        "status": "В наличии",
    },
    {
        "id": "i9j0k1l2-m3n4-5678-ijkl-m90123456789",
        "title": "Сияние",
        "author": "Стивен Кинг",
        "year": "1977",
        "status": "В наличии",
    },
    {
        "id": "j0k1l2m3-n4o5-6789-jklm-n01234567890",
        "title": "Маленький принц",
        "author": "Антуан де Сент-Экзюпери",
        "year": "1943",
        "status": "В наличии",
    },
]


@pytest.fixture
def test_create_data_json():
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(test_data, file, ensure_ascii=False, indent=4)
    yield Data_library(file_path)
    os.remove(file_path)


def test_add_book(test_create_data_json):
    library = test_create_data_json
    library.add_book(title="Fite club", author="Счак Поланник", year="1996")
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert data[-1]["title"] == "Fite club"
    assert data[-1]["author"] == "Счак Поланник"
    assert data[-1]["year"] == "1996"


def test_truncate_book(test_create_data_json):
    library = test_create_data_json
    library.truncate_book("j0k1l2m3-n4o5-6789-jklm-n01234567890")
    with pytest.raises(IdNotFound):
        library.search_book_by_id("j0k1l2m3-n4o5-6789-jklm-n01234567890")


def test_search_book(test_create_data_json):
    library = test_create_data_json
    assert library.search_book(title="Мастер и Маргарита") == [
        {
            "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "title": "Мастер и Маргарита",
            "author": "Булгаков",
            "year": "1967",
            "status": "Выдан",
        }
    ]


def test_fetch_all_books(test_create_data_json):
    library = test_create_data_json
    assert library.fetch_all_books() == test_data


def test_change_status_book(test_create_data_json):
    library = test_create_data_json
    library.change_status("a1b2c3d4-e5f6-7890-abcd-ef1234567890", "В наличии")
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert data[0]["status"] == "В наличии"
