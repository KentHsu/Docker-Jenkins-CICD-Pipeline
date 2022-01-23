db.createUser({
  user: "graphql-user",
  pwd: "graphql-pwd",
  roles: [
    {
      role: "readWrite",
      db: "graphql",
    }
  ],
});

db = new Mongo().getDB("graphql");
db.createCollection("books", { capped: false });
db.books.insert([
  {"name": "Name of the Wind", "genre": "Fantasy", "id": "1", "authorId": "1"},
  {"name": "The Final Empire", "genre": "Fantasy", "id": "2", "authorId": "2"},
  {"name": "The Long Earth", "genre": "Sci-Fi", "id": "3", "authorId": "3"},
]);

db.createCollection("authors", { capped: false });
db.authors.insert([
    {"name": "Patrick Rothfuss", "age": 44, "id": "1"},
    {"name": "Brandon Sanderson", "age": 42, "id": "2"},
    {"name": "Terry Pratchett", "age": 66, "id": "3"},
])
