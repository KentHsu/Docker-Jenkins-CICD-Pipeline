from graphene import ObjectType, Schema, Field
from graphene import ID, String, Int, List
from database.mongodb import connect_to_mongodb


db = connect_to_mongodb()

class BookType(ObjectType):
    id = ID()
    name = String()
    genre = String()
    author = List(lambda: AuthorType)

    def resolve_author(parent, info):
        return list(db.authors.find({"id": parent["authorId"]}))


class AuthorType(ObjectType):
    id = ID()
    name = String()
    age = Int()
    books = List(BookType)

    def resolve_books(parent, info):
        return list(db.books.find({"authorId": parent["id"]}))


class RootQuery(ObjectType):

    book = Field(BookType, id=ID())
    author = Field(AuthorType, id=ID())
    books = Field(List(BookType))
    authors = Field(List(AuthorType))

    def resolve_book(parent, info, id):
        return db.books.find_one({"id": id})

    def resolve_author(parent, info, id):
        return db.authors.find_one({"id": id})

    def resolve_books(parent, info):
        return list(db.books.find({}))

    def resolve_authors(parent, info):
        return list(db.authors.find({}))


def graphql_schema():
    schema = Schema(query=RootQuery)
    return schema
