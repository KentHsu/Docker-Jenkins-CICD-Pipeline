FROM mongo:latest

ARG BUILD_NUMBER=0
ARG BUILD_TAG=local
LABEL build_number=${BUILD_NUMBER}
LABEL build_tag=${BUILD_TAG}

COPY ./init-mongo.js /docker-entrypoint-initdb.d
COPY ./secrets/username /run/secrets/mongo_admin_username
COPY ./secrets/password /run/secrets/mongo_admin_password
