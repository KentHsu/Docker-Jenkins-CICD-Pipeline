from flask import Flask
from flask_graphql import GraphQLView
from schema.schema import graphql_schema


app = Flask(__name__)


app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=graphql_schema(), graphiql=True),
)


@app.route("/")
def index():
    return "hello, world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
