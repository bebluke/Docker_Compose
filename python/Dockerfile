FROM python:latest

WORKDIR /app


COPY requirements.txt requirements.txt
RUN install -r requirements.txt

COPY . .

EXPOSE 5000

CMD["python", "app.py"]
