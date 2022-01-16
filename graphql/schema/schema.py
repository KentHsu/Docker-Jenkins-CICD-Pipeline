from graphene import ObjectType, Schema, Field
from graphene import ID, String, Int


books = [
    {"name": "Name of the Wind", "genre": "Fantasy", "id": "1"},
    {"name": "The Final Empire", "genre": "Fantasy", "id": "2"},
    {"name": "The Long Earth", "genre": "Sci-Fi", "id": "3"},
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


class AuthorType(ObjectType):
    id = ID()
    name = String()
    age = Int()


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
