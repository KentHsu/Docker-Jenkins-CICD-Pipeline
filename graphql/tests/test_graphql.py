from graphene.test import Client
import pytest
from schema.schema import graphql_schema


@pytest.fixture
def client():
    client = Client(graphql_schema())
    return client


def test_book(client):
    executed = client.execute(
        """
        {
          book(id: "1") {
            id
            name
            genre
          }
        }
    """
    )
    assert executed == {
        "data": {"book": {"id": "1", "name": "Name of the Wind", "genre": "Fantasy"}}
    }


def test_author(client):
    executed = client.execute(
        """
        {
          author(id: "1") {
            id
            name
            age
          }
        }
    """
    )
    assert executed == {
        "data": {"author": {"id": "1", "name": "Patrick Rothfuss", "age": 44}}
    }
