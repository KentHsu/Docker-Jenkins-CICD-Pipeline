from graphene import ObjectType, Schema, Field
from graphene import ID, String, List


books = [
    { "name": 'Name of the Wind', "genre": 'Fantasy', "id": '1' },
    { "name": 'The Final Empire', "genre": 'Fantasy', "id": '2' },
    { "name": 'The Long Earth', "genre": 'Sci-Fi', "id": '3' },
]

class BookType(ObjectType):
    id = ID()
    name = String()
    genre = String()


class RootQuery(ObjectType):

    book = Field(BookType, id = ID())

    def resolve_book(parent, info, id):
        for book in books:
            if book["id"] == id:
                return book
        return None


def graphql_schema():
    schema = Schema(
        query=RootQuery
    )
    return schema
