FROM python:3.9-alpine as builder

ARG BUILD_NUMBER=0
ARG BUILD_TAG=local
LABEL build_number=${BUILD_NUMBER}
LABEL build_tag=${BUILD_TAG}

WORKDIR /app

COPY Pipfile.* .

RUN pip install --user pipenv

ENV PIPENV_VENV_IN_PROJECT=1

RUN /root/.local/bin/pipenv sync


FROM python:3.9-alpine as runtime

WORKDIR /app

COPY --from=builder /app/.venv ./venv

COPY . .

CMD [ "./venv/bin/python3", "app.py", "--host", "0.0.0.0", "--port", "4000"]
