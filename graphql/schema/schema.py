from graphene import ObjectType, Schema, String


class Hello(ObjectType):

    hello = String(name=String(default_value="stranger"))

    def resolve_hello(root, info, name):
        return f"Hello, {name}"


def graphql_schema():
    schema = Schema(
        query=Hello
    )
    return schema
