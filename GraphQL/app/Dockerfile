FROM python:3.8 

CMD [ "pipenv", "run", "python3", "app.py", "--host", "0.0.0.0", "--port", "5000"]

WORKDIR /src
COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv && pipenv sync

COPY . .
