from graphene import ObjectType, Schema, Field
from graphene import ID, String, Int, List


books = [
    {"name": "Name of the Wind", "genre": "Fantasy", "id": "1", "authorId": "1"},
    {"name": "The Final Empire", "genre": "Fantasy", "id": "2", "authorId": "2"},
    {"name": "The Long Earth", "genre": "Sci-Fi", "id": "3", "authorId": "3"},
]

authors = [
    {"name": "Patrick Rothfuss", "age": 44, "id": "1"},
    {"name": "Brandon Sanderson", "age": 42, "id": "2"},
    {"name": "Terry Pratchett", "age": 66, "id": "3"},
]


class BookType(ObjectType):
    id = ID()
    name = String()
    genre = String()
    author = List(lambda: AuthorType)

    def resolve_author(parent, info):
        result = []
        for author in authors:
            if author["id"] == parent["authorId"]:
                result.append(author)
        return result


class AuthorType(ObjectType):
    id = ID()
    name = String()
    age = Int()
    books = List(BookType)

    def resolve_books(parent, info):
        result = []
        for book in books:
            if book["authorId"] == parent["id"]:
                result.append(book)
        return result


class RootQuery(ObjectType):

    book = Field(BookType, id=ID())
    author = Field(AuthorType, id=ID())

    def resolve_book(parent, info, id):
        for book in books:
            if book["id"] == id:
                return book
        return None

    def resolve_author(parent, info, id):
        for author in authors:
            if author["id"] == id:
                return author
        return None


def graphql_schema():
    schema = Schema(query=RootQuery)
    return schema
