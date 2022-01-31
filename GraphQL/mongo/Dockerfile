FROM mongo:latest

COPY ./init-mongo.js /docker-entrypoint-initdb.d
COPY ./secrets/username /run/secrets/mongo_admin_username
COPY ./secrets/password /run/secrets/mongo_admin_password
