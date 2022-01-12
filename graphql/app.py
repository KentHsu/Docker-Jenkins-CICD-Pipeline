from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema


app = Flask(__name__)

class Hello(ObjectType):

    hello = String(name=String(default_value="stranger"))

    def resolve_hello(root, info, name):
        return f"Hello, {name}"

schema = Schema(query=Hello)

app.add_url_rule('/graphql',\
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.route("/")
def index():
    return "hello, world"


if __name__ == "__main__":
    app.run()
