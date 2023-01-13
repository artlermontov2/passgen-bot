FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

ENV BOT_TOKEN=5636485810:AAGQDSmlzrt9SjZKkd9U-NAxVeOw8jsdVL8

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]