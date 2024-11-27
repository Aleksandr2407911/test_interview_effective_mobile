import argparse
from main import Data_library

parser = argparse.ArgumentParser(description="Library manager system")
subparser = parser.add_subparsers(dest="command", help="Available commands")

add_parser = subparser.add_parser("add", help="Add a new book")
add_parser.add_argument(
    "-t", "--title", type=str, required=True, help="title of the book"
)
add_parser.add_argument(
    "-a", "--author", type=str, required=True, help="author of the book"
)
add_parser.add_argument(
    "-y", "--year", type=str, required=True, help="Year of the book"
)

truncate_parser = subparser.add_parser("truncate", help="Truncate a book")
truncate_parser.add_argument("-i", "--id", type=str, required=True, help="If of book")

search_parser = subparser.add_parser("search", help="Search a books")
search_parser.add_argument(
    "-t", "--title", type=str, required=False, help="title of the book"
)
search_parser.add_argument(
    "-a", "--author", type=str, required=False, help="author of the book"
)
search_parser.add_argument(
    "-y", "--year", type=str, required=False, help="Year of the book"
)

fetch_all_books_parser = subparser.add_parser(
    "list", help="Fitch all books from database"
)

change_stase_parser = subparser.add_parser("change-status", help="Truncate a book")
change_stase_parser.add_argument(
    "-i", "--id", type=str, required=True, help="If of book"
)
change_stase_parser.add_argument(
    "-s", "--status", type=str, required=True, help="Status of book"
)

args = parser.parse_args()

library = Data_library("data.json")

try:
    if args.command == "add":
        if not args.title or not args.author or not args.year:
            print("Title, author and year must be provided to add a book.")
        else:
            print(library.add_book(args.title, args.author, args.year))

    if args.command == "truncate":
        if not args.id:
            print("For truncate the book you must be provided book id")
        else:
            print(library.truncate_book(args.id))

    if args.command == "search":
        if not args.title and not args.author and not args.year:
            print("Title, author and year must be provided to search a book.")
        else:
            print(
                library.search_book(
                    title=args.title, author=args.author, year=args.year
                )
            )

    if args.command == "list":
        print(library.fetch_all_books())

    if args.command == "change-status":
        if args.status not in ("Выдан", "В наличии") or not args.id:
            print("Status and id must be provided for change status books")
        else:
            print(library.change_status(book_id=args.id, new_status=args.status))

except Exception as e:
    print(f"Error: {e}")
